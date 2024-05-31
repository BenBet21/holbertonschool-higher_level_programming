#!/usr/bin/env python3
"""Develop a Simple API using Python with Flask"""
from flask import Flask, request, jsonify
from flask import jsonify
import json

app = Flask(__name__)
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    return "OK"


@app.route("/data")
def data():
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route('/users/<username>')
def get_users(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    if not request.json or "username" not in request.json:
        return jsonify({"error": "Username is required"}), 400

    user_data = request.json
    username = user_data["username"]
    users[username] = {
        "username": user_data.get("username"),
        "name": user_data.get("name"),
        "age": user_data.get("age"),
        "city": user_data.get("city")
    }
    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == '__main__':
    app.run(debug=True)
