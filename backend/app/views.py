from app import address
from app import naturalgas
from app import electricity
from app import app
from flask import json, request

# Sets up the routes, really

from flask import render_template

# Sets up the routes, really

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/house', methods=['GET'])
def houseNoAddress():
	return render_template('house.html', address=request.args.get('address'))

@app.route('/house/<addrs>', methods=['GET'])
def houseWAddress():
	houseId = json.jsonify({"info": address.getId(addrs)})
	return render_template('house.html', id = houseId, variable2 = "hello" )

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

@app.route('/streetelect/<addrs>')
def avgstreet(addrs):
	return json.jsonify({"electricity": electricity.streetElectricity(addrs)})
