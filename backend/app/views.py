from app import address
from app import app
from flask import json

# Sets up the routes, really

@app.route('/address.json')
def someAddresses():
    all = []
    all.append(address.findOneByID(22))
    all.append(address.findOneByID(24))
    all.append(address.findOneByID(26))
    all.append(address.findOneByID(10021))
    return json.jsonify({"addresses": all})
