from app import address
from app import naturalgas
from app import electricity
from app import codeviolation
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
	houseInfo = json.jsonify({"info": address.getInfo(addrs)})
	houseElect = json.jsonify({"electricity": electricity.findElectricity(addrs)})
	houseGas = json.jsonify({"NaturalGas": naturalgas.findNatGas(addrs)})
   #houseWater = json.jsonify({"Water": water.findWater(addrs)})
	houseCodeVio = json.jsonify({"CodeViolation": codeviolation.findCodeVio(addrs)})


	streetCodeVio = json.jsonify({"StreetCodeViolation": codeviolation.streetCodeVio(addrs)})

	totalCityElect = json.jsonify({"totalCityElect": electricity.cityTotalElect})
	totalCityNatGas = json.jsonify({"totalCityNatGas": naturalgas.cityTotalNatGas})
	#totalCityWater = json.jsonify({"totalCityWater": water.cityTotalWater})


	avgCityElect = json.jsonify({"avgCityElect": electricity.cityAvgElect()})
	avgCityNatGas = json.jsonify({"avgCityNatGas": naturalgas.cityAvgNatGas()})
	#avgCityWater = json.jsonify({"avgCityWater": water.cityAvgWater})


	avgStreetElect = json.jsonify({"avgStreetElect": electricity.streetElectricity(addrs)})
	avgStreetNatGas = json.jsonify({"avgStreetNatGas": naturalgas.streetNatGas(addrs)})
	#avgStreetWater = json.jsonify({"avgCityWater": water.streetWater(addrs)})

	print(houseInfo)
	print(houseElect)
	print(houseGas)

	data = { houseInfo, houseElect, houseGas }

	#return json.jsonify({"data": data})
	return render_template('house.html', data = {houseInfo, houseElect,
			houseGas, houseCodeVio, streetCodeVio,avgCityElect, 
			avgCityNatGas, avgStreetElect, avgStreetNatGas});

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
