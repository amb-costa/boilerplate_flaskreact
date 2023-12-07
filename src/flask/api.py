# Building API with JWT token for admin mode
# Using CRUD principles!
# Any function that works on the "/" route will be located on the app.py file

from flask import Flask, request, jsonify, url_for, Blueprint, json
from models import db, Tasks, Errors
from template.exceptions import generate_sitemap, APIException
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from datetime import timedelta

api = Blueprint('api', __name__)

@api.route("/maintest", methods=['GET'])
def maintest(): 
    try:
        tasks = Tasks.query.all()
        tasks_list = list(map(lambda single_task : single_task.task, tasks))
        return jsonify({"tasks" : tasks_list}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "no data yet"}), 204
    
@api.route("/errors", methods=['GET'])
def errordisplay():
    try:
        errors = Errors.query.all()
        single_error = list(map(lambda error:errors.number), errors)
        single_description = list(map(lambda desc:desc.description), errors)
        return jsonify({"error number": single_error, "error description": single_description})
    except Exception as e:
        print(e)
        return jsonify({"message" : "no errors to display"}), 204
