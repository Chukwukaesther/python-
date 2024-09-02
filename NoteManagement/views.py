from flask import jsonify, request, session
from datetime import datetime
from functools import wraps
from models import notes, users
from werkzeug.security import generate_password_hash, check_password_hash


def register():
    data = request.get_json()
    username = data.get('username', '').strip().lower()
    password = data.get('password', '').strip()

    if not username or not password:
        return jsonify({'message': 'Username and password cannot be empty'}), 400

    if users.find_one({'username': username}):
        return jsonify({'message': 'Username already exists'}), 409

    new_password = generate_password_hash(password)
    user1 = {'username': username, 'password': new_password}
    users.insert_one(user1)
    return jsonify({'message': 'User successfully registered'}), 201


def login():
    data = request.get_json()
    username = data.get('username', '').strip().lower()
    password = data.get('password', '').strip()

    user = users.find_one({'username': username})

    if user and check_password_hash(user['password'], password):
        return jsonify({'message': 'Login successfully'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401


def create_note():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    author = data.get('author')

    if notes.find_one({"title": title, "author": author}):
        return jsonify({"message": "Note already exists"}), 409
    else:
        new_note = {"title": title, "author": author, "content": content}
        notes.insert_one(new_note)
        return jsonify({"message": "Note created successfully"}), 201


def update_note():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')

    result = notes.update_one({'title': title}, {'$set': {'content': content}})

    if result.matched_count > 0:
        return jsonify({'message': 'Note updated successfully'}), 200
    else:
        return jsonify({'message': 'Note not found'}), 404


def delete_note():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    author = data.get('author')

    result = notes.delete_one({'title': title, 'content': content, 'author': author})

    if result.deleted_count > 0:
        return jsonify({'message': 'Note deleted successfully'}), 200
    else:
        return jsonify({'message': 'Note not found'}), 404


def add_note():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    author = data.get('author')

    if not title or not content or not author:
        return jsonify({'message': 'Title, content, and author cannot be empty'}), 400

    new_note = {"title": title, "content": content, "author": author}
    notes.insert_one(new_note)
    return jsonify({'message': 'Note added successfully'}), 201


def logout():
    data = request.get_json()
    password = data.get('password')
    if not password == password:
        return jsonify({'message': 'incorrect password'})
    else:
        return jsonify({'message': 'successfully logged out'})
