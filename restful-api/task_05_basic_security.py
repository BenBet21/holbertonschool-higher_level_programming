#!/usr/bin/env python3
"""API Security and Authentication Techniques"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps


SECRET_KEY = "Last_Christmas"
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
auth = HTTPBasicAuth()

users = {
      "user1": {"username": "Benoit", "password": "<love>", "role": "user"},
      "admin1": {"username": "Ben", "password": "<war>", "role": "admin"}
  }


@auth.verify_password
def verify_password(username, password):
    """Verify the password of the user"""

    if (username in users and
            check_password_hash(users.get(username), password)):
        return username


@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    if auth:
        user_password = users.get(auth.username)['password']
    if check_password_hash(user_password, auth.password):
        token = jwt.encode({
            'user': auth.username,
            'role': users[auth.username]['role'],
        }, app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({'token': token})

    return jsonify({'message': 'Could not verify'}), 401


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'Token is missing!'}), 403

        try:
            data = (jwt.decode(token, app.config['SECRET_KEY'],
                               algorithms=["HS256"]))
            current_user = data['user']
            current_role = data['role']
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token is invalid!'}), 403

        return f(current_user, current_role, *args, **kwargs)

    return decorated


@app.route('/protected', methods=['GET'])
@token_required
def protected(current_user, current_role):
    return jsonify({'message': f'Hello, {current_user}!
                    Your role is {current_role}'})


def role_required(required_role):
    def decorator(f):
        @wraps(f)
        def decorated_function(current_user, current_role, *args, **kwargs):
            if current_role != required_role:
                return jsonify({'message':
                                'Access denied: insufficient permissions'}),
            return f(current_user, current_role, *args, **kwargs)
        return decorated_function
    return decorator


@app.route('/admin', methods=['GET'])
@token_required
@role_required('admin')
def admin_route(current_user, current_role):
    return jsonify({'message': f'Welcome, {current_user}.
                    Your role is {current_role}. This is an admin route.'})


@app.route('/user', methods=['GET'])
@token_required
@role_required('user')
def user_route(current_user, current_role):
    return jsonify({'message': f'Welcome, {current_user}.
                    Your role is {current_role}. This is a user route.'})


if __name__ == '__main__':
    app.run(debug=True)
