from flask import Flask
from models import models

class ToDo:
    def __init__(self):
        self._tasks = [
            {"id" : 1,
             "task" : "laundry day",
             "created_at": "today"}
        ]

    

