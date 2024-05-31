#!/usr/bin/env python3
"""Develop a Simple API using Python with Flask"""
from flask import Flask
from flask import jsonify, request, Response
from collections import OrderedDict
import json

app = Flask(__name__)

users = {}

@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/status')
def status():
    return "OK"


@app.route('/data')
def get_usernames():
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        ordered_user = OrderedDict([
            ("username", user["username"]),
            ("name", user["name"]),
            ("age", user["age"]),
            ("city", user["city"])
        ])
        return Response(json.dumps(ordered_user), mimetype='application/json')
    else:
        return jsonify({"error": "User not found"})


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON data provided"})

    username = data.get('username')
    if not username:
        return jsonify({"error": "User not found"})

    if username in users:
        return jsonify({"error": "Username already exists"})

    users[username] = {
        "username": data.get('username', ''),
        "name": data.get('name', ''),
        "age": data.get('age', 0),
        "city": data.get('city', '')
    }
    ordered_user = OrderedDict([
                ("username", users[username]["username"]),
                ("name", users[username]["name"]),
                ("age", users[username]["age"]),
                ("city", users[username]["city"])
            ])
    users[username] = dict(ordered_user)
    response = {
        "message": "User added successfully",
        "user": ordered_user
    }
    return Response(json.dumps(response), mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)
