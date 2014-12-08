from app import address
from app import naturalgas
from app import electricity
from app import codeviolation
from app import totaltuples
from app import water
from app import app

from flask import json, request

# Sets up the routes, really

from flask import render_template

# Sets up the routes, really

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/house/<addrs>')
def houseWAddress(addrs):
	data = {
		"addrs":		addrs,
		"info": 		address.getInfo(addrs),

		"electricity": 		electricity.findElectricity(addrs),
		"totalCityElec":	electricity.cityTotalElect(),
		"avgCityElec":		electricity.cityAvgElect(),	
		"avgStreetElec":	electricity.streetElectricity(addrs),

		"naturalGas":		naturalgas.findNatGas(addrs),
		"totalCityNatGas":	naturalgas.cityTotalNatGas(),
		"avgStreetNatGas":	naturalgas.streetNatGas(addrs),

		"water":		water.findWater(addrs),
		"totalCityWater":	water.cityTotalWater(),
		"avgCityWater":		water.cityAvgWater(),
		"avgStreetWater":	water.streetWater(addrs),

		"codeViolation":	codeviolation.findCodeVio(addrs),
		"streetCodeViolation":	codeviolation.streetCodeVio(addrs)
	}

	return render_template('house.html', data = data )


@app.route('/data/<addrs>')
def houseData(addrs):
	data = {
                "addrs":                addrs,
		"info":                 address.getInfo(addrs),

		"electricity":          electricity.findElectricity(addrs),
		"totalCityElec":        electricity.cityTotalElect(),
		"avgCityElec":          electricity.cityAvgElect(),
		"avgStreetElec":        electricity.streetElectricity(addrs),

		"naturalGas":           naturalgas.findNatGas(addrs),
		"totalCityNatGas":      naturalgas.cityTotalNatGas(),
		"avgStreetNatGas":      naturalgas.streetNatGas(addrs),

		"water":                water.findWater(addrs),
		"totalCityWater":       water.cityTotalWater(),
		"avgCityWater":         water.cityAvgWater(),
		"avgStreetWater":       water.streetWater(addrs),

		"codeViolation":        codeviolation.findCodeVio(addrs),
		"streetCodeViolation":  codeviolation.streetCodeVio(addrs)
	}

	return json.jsonify({ "data": data })

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

@app.route('/codeViolation/<addrs>')
def getCodeVio(addrs):
	return json.jsonify({"codeViolation": codeviolation.findCodeVio(addrs)})

@app.route('/codeViolationStreet/<addrs>')
def getCodeVioStreet(addrs):
	return json.jsonify({"codeViolation": codeviolation.streetCodeVio(addrs)})

@app.route('/TUPLES')
def totalTuples():
	return json.jsonify({"totalTuples": totaltuples.totalTuples()})

@app.route('/Water/<addrs>')
def totalTuples(addrs):
	return json.jsonify({"waterpls": water.findWater(addrs)})
