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

# POST: JSON will arrive as "task" and "due_at"
# create a new Tasks instance and commit
@api.route("/maintest", methods=['POST'])
def post_test():
    try:
        task = request.json.get("task")
        due_at = request.json.get("due_at")
        newPost = Tasks(task = task, due_at = due_at)
        db.session.add(newPost)
        db.session.commit()
        return jsonify({"HTTP_status": "task added to database!"}), 201
    except Exception as e:
        print(e)
        return jsonify({"HTTP_status": "try later"})

# GET: JSON will have no particular data
# deliver all tasks and due date
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

# PUT: JSON will have to specify an ID to identify a specific task
# successfully updates according to id
@api.route('/maintest/<int:id>', methods=['PUT'])
def put_test(id):
    try:
        task = request.json.get("task")
        due_at = request.json.get("due_at")
        original_task = Tasks.query.get(id)
        original_task.task = task
        original_task.due_at = due_at
        db.session.commit()
        return jsonify({"HTTP_status" : "successful update"}), 202
    except Exception as e:
        print(e)
        return jsonify({"HTTP_status": "something happened"})

# DELETE: using a loop to delete instead of whole at once
# to avoid "Class 'builtins.list' is not mapped" line at terminal
@api.route("/maintest", methods=["DELETE"])
def delete_test():
    try:
        tasks = Tasks.query.all()
        for task in tasks:
            db.session.delete(task)
        db.session.commit()
        return jsonify({"HTTP_status" : "all data cleared"}), 202
    except Exception as e:
        print(e)
        return jsonify({"HTTP_status": "no data yet"}), 204    
    

@api.route("/errors", methods=['GET'])
def errordisplay():
    try:
        errors = Errors.query.all()
        single_error = list(map(lambda error : error.number), errors)
        single_description = list(map(lambda desc : desc.description), errors)
        return jsonify({"error_number": single_error, "error_description": single_description}), 200
    except Exception as e:
        print(e)
        return jsonify({"HTTP_status" : "no errors to display"}), 204
    
