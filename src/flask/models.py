from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Tasks: main model to develop CRUD functionalities through a task to-do list
# id, task, edited_at
# NEXT: RESEARCH HOW TO ADD TIME AND FORMAT
class Tasks(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(250), nullable=False)
    edited_at = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Tasks %r>' % self.id
    
    def serialize(self):
        return {
            "id" : self.id,
            "task" : self.task,
            "edited at": self.edited_at
        }


# Errors: main model to store HTML errors, to render them as a cheatcode using React
# id, number, description
class Errors(db.Model):
    __tablename__ = "errors"
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True, nullable=False)
    description = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return '<Errors %r>' % self.id
    
    def serialize(self):
        return {
            "id": self.id,
            "number error": self.number,
            "error description" : self.description
        }