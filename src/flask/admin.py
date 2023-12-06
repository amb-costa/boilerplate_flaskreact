# Admin : basic view to further develop admin functionalities
# Heavily inspired on https://github.com/amb-costa/starwarsRESTAPI.py/blob/main/src/admin.py
# Check the flask_admin documentation for more info on admin view + styling

import os
from flask_admin import Admin
from models import db, Tasks, Errors
from flask_admin.contrib.sqla import ModelView


def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'solar'
    admin = Admin(app, name='Task Master', template_mode='bootstrap3')

    admin.add_view(ModelView(Tasks, db.session))
    admin.add_view(ModelView(Errors, db.session))
