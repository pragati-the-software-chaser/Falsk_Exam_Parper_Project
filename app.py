import json
import os
import connexion
from flask import Flask ,request, jsonify
# Create the application instance
app = connexion.App(__name__, specification_dir='swagger/')
# Read the swagger.yml file to configure the endpoints
app.add_api('/Users/pragatigupta/flask-test/swagger.yml')
#app = Flask(__name__)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)