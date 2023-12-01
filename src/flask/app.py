# os: environment library, used to generate a specific port
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main(): 
    return {"message": "flask is running"}

# generating port 3001 for the main page
# using os.environ.get, we add a port object for flask to run
if __name__ == "__main__":
    PORT = int(os.environ.get('PORT', 3001))
    app.run(host='0.0.0.0', port=PORT, debug=True)