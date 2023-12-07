# os: environment library, used to generate a specific port
# cors: cross origin to solve any issues connecting with frontend
# .base: 404 error + auxiliary index.html file
import os
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS, cross_origin
from template.exceptions import APIException, generate_sitemap
from models import db, Tasks
from api import api


ENV = "development" if os.getenv("FLASK_DEBUG") == "1" else "production"
static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'template/')

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Creating the databases calling the db SQLAlchemy component inside models file
db.init_app(app)
with app.app_context():
    db.create_all()

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints

@app.route('/')
def sitemap():
    # this should run the test view according to generate_sitemap
    if ENV == "development":
        return generate_sitemap(app)
    # sends to index but first create data on the tasks part
    
    return send_from_directory(static_file_dir,"index.html")

app.register_blueprint(api)

# generating port 3001 for the main page
# using os.environ.get, we add a port object for flask to run
if __name__ == "__main__":
    PORT = int(os.environ.get('PORT', 3001))
    app.run(host='0.0.0.0', port=PORT, debug=True)