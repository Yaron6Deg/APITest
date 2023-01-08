import flask
from flask import Flask
from flask_cors import CORS, cross_origin
import requests



app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

@app.route('/')
def hello_world():
    url = "https://jsonplaceholder.typicode.com/todos/1"
#    url = "https://6degrees-app-dev.galencloud.com/HealthCheck"

    payload = ""
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
#    api_url = "https://6degrees-app-dev.galencloud.com/HealthCheck"
#    response = requests.get(api_url)
#    response.json()
#    response.status_code
#    response.headers["Content-Type"]
    return response.text
