from app import address
from app import naturalgas
from app import electricity
from app import app
from flask import json

# Sets up the routes, really

from flask import render_template

# Sets up the routes, really

@app.route('/')
def main():
	return render_template('index.html')

# @app.route('/house')
# def houseNoAddress():
#	return render_template('house.html')

@app.route('/address/<id>')
def addressId(id):
    return json.jsonify({"addresses": address.findOneByID(id)})

@app.route('/getAddressId/<addrs>')
def getAddressId(addrs):
    return json.jsonify({"addressId": address.getId(addrs)})

@app.route('/naturalgas/<id>')
def naturalGasId(id):
    return json.jsonify({"naturalgas": naturalgas.findOneByID(id)})

@app.route('/electricity/<addrs>')
def whatsuphomie(addrs):
	return json.jsonify({"electricity": electricity.findElectricity(addrs)})
