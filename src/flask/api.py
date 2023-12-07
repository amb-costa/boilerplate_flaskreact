# Building API with JWT token for admin mode
# Using CRUD principles!
# Any function that works on the "/" route will be located on the app.py file

from flask import Flask, request, jsonify, url_for, Blueprint, json
from models import db, Tasks, Errors
from template.exceptions import generate_sitemap, APIException
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from datetime import timedelta

api = Blueprint('api', __name__)

# CRUD: Create Read Update Delete
# POST GET PUT DELETE
# Errors won't have CRUD functionalities, since it's a cheatlist

@api.route("/maintest", methods=['POST'])
def post_test():
    data = request.get_json()
    newPost = Tasks(task = data.task, due_at = data.due_at)
    db.session.add(newPost)
    db.session.commit()
    return jsonify({"HTTP_status": "task added to database!"}), 201

@api.route("/maintest", methods=['GET'])
def get_test(): 
    try:
        tasks = Tasks.query.all()
        tasks_list = list(map(lambda single_task : single_task.task, tasks))
        due_list = list(map(lambda due: due.due_at, tasks))
        return jsonify({"tasks" : tasks_list, "due_at" : due_list}), 200
    except Exception as e:
        print(e)
        return jsonify({"HTTP_status": "no data yet"}), 204
    
@api.route("/errors", methods=['GET'])
def errordisplay():
    try:
        errors = Errors.query.all()
        single_error = list(map(lambda error : error.number), errors)
        single_description = list(map(lambda desc : desc.description), errors)
        return jsonify({"error_number": single_error, "error_description": single_description})
    except Exception as e:
        print(e)
        return jsonify({"HTTP_status" : "no errors to display"}), 204
    
# special route to delete whole database for cleaning purposes
@api.route("/delete", methods=["DELETE"])
def deletedisplay():
    try:
        tasks = Tasks.query.all()
        db.session.delete(tasks)
        db.session.commit()
    except Exception as e:
        print(e)
        return jsonify({"HTTP_status": "no data yet"}), 204