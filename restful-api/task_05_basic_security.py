#!/usr/bin/env python3
"""API Security and Authentication Techniques"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_identity
)
from functools import wraps


SECRET_KEY = "Last_Christmas"
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['JWT_SECRET_KEY'] = SECRET_KEY  # Utilisé par Flask-JWT-Extended
auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Verify the password of the user"""
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return jsonify({'message': 'Basic Auth: Access Granted'})


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Invalid credentials'}), 401

    username = data['username']
    password = data['password']
    user = users.get(username)
    
    if user and check_password_hash(user['password'], password):
        token = create_access_token(identity={'username': username, 'role': user['role']})
        return jsonify({'access_token': token})

    return jsonify({'message': 'Invalid username or password'}), 401


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    current_user = get_jwt_identity()
    return jsonify({'message': f'JWT Auth: Access Granted, {current_user["username"]}'})


def role_required(required_role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            current_user = get_jwt_identity()
            if current_user['role'] != required_role:
                return jsonify({'message': 'Access denied: insufficient permissions'}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator


@app.route('/admin-only', methods=['GET'])
@jwt_required()
@role_required('admin')
def admin_route():
    current_user = get_jwt_identity()
    return jsonify({'message': f'Admin Access: Granted, {current_user["username"]}'})


# Gestionnaires d'erreurs JWT
@jwt.unauthorized_loader
def handle_unauthorized_error():
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error():
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error():
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error():
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error():
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run(debug=True)
