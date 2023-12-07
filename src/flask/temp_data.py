# i will create a set of commands here to test functionalities

import click
from models import db, Tasks

"""
In this file, you can add as many commands as you want using the @app.cli.command decorator
Flask commands are usefull to run cronjobs or tasks outside of the API but sill in integration 
with youy database, for example: Import the price of bitcoin every night as 12am
"""
def setup_commands(app):
    
    """ 
    This is an example command "insert-test-users" that you can run from the command line
    by typing: $ flask insert-test-users 5
    Note: 5 is the number of users to add
    """
    @app.cli.command("add-tasks") # name of our command
    @click.argument() # argument of out command
    def addTasks():
        print("Creating test users")
        task1 = Tasks()
        task1.id=1
        task1.task="doing laundry"
        task1.created_at="today"
        print(task1)
        db.session.add(task1)
        task2 = Tasks()
        task2.id=2
        task2.task="buying groceries"
        task2.created_at="this morning"
        db.session.add(task2)
        db.session.commit()
        print(Tasks.query.all())

        print("All test users created")

        ### Insert the code to populate others tables if needed

