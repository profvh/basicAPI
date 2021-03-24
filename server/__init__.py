import os
from flask import Flask, request, make_response, jsonify
from flask_restful import Api

from flask_cors import CORS
import os


app = Flask(__name__)
api = Api(app)
CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['JSON_AS_ASCII'] = False

respE = {
        "events":[
            {
                "titulo":"Semana acadêmica",
                "data":"24/03/2021"
            },
            {
                "titulo":"Semana da computação",
                "data":"30/08/2021"
            },
            {
                "titulo":"Maratona de programação",
                "data":"30/08/2022"
            }
        ]
    }

@app.route('/events',methods=['GET'])
def events():
    resp = respE

    return make_response(jsonify(resp)), 200

@app.route('/events',methods=['POST'])
def new_events():
    content = request.json
    ne = {
        "titulo":content['titulo'],
        "data":content['data']
    }
    respE['events'].append(ne)
    return "ok"

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Headers','Content-Type, UserCredential, PortalCredential, Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,PATCH,OPTIONS')

    return response

