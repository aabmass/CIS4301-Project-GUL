from app import address
from app import app
from flask import json

# Sets up the routes, really

@app.route('/address/<id>')
def someAddresses(id):
    return json.jsonify({"addresses": address.findOneByID(id)})
