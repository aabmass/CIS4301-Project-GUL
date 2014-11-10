from app import app
from app import models
from flask import json as json

@app.route('/')
@app.route('/index')
def index():
    return json.jsonify(name='Ruth', age=22, snoutLength={"puplet" :True})

@app.route('/country')
def country():
     all = models.Country.findAll()
     return json.jsonify({"results": all})
