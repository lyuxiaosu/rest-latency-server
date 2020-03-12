## TO INSTALL FLASK
 ## Optional: setup a virtual environment
 # python3 -m venv venv
 # . venv/bin/activate
 ## Install Flask and the requests package
 # pip install Flask
 # pip install requests
### TO RUN FLASK
 # export FLASK_APP=gateway.py
 # flask run

import json
from flask import Flask
app = Flask(__name__)

import requests

@app.route('/')
def hello_world():
    req = requests.get("http://localhost:8080/request")
    req_dict = json.loads(str(req.text))
    print(req_dict['data'])
    return '<html><body> I RESTed for ' + str(req_dict['data']) + ' time units. </body></html>\n'
