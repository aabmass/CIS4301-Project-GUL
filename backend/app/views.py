from app import app
from app import models
from flask import json as json

""" Sets up the routes, really """

@app.route('/address')
def address():
     all = models.Address.findAll()
     print all
     return json.jsonify({"addresses": all})
