from flask import Blueprint, session, jsonify
from views import create_note, register, login, update_note, delete_note, add_note

esther = Blueprint('api', __name__)


@esther.route("/create_note", methods=["POST"])
def create_note_route():
    return create_note()


@esther.route("/register", methods=["POST"])
def register_route():
    return register()


@esther.route("/login", methods=["POST"])
def login_route():
    return login()


@esther.route("/update_note", methods=["POST"])
def update_note_route():
    return update_note()


@esther.route("/delete_note", methods=["POST"])
def delete_note_route():
    return delete_note()


@esther.route("/add_note", methods=["POST"])
def add_note_route():
    return add_note()
