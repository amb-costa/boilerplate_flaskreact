# os: environment library
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main(): 
    return print("flask is running!")

if "__name__" == "__main__":
    PORT = int(os.environ.get('PORT', 3001))
    app.run(host='0.0.0.0', port=PORT, debug=True)