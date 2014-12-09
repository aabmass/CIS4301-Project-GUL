from app import address
from app import naturalgas
from app import electricity
from app import codeviolation
from app import totaltuples
from app import water
from app import funFacts
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
	info = address.getInfo(addrs)
	if info == "N/A":
			return render_template('not_found.html', addrs = info)
			
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
		"avgCityNatGas":	naturalgas.cityAvgNatGas(),

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




@app.route('/FunFactsData/')
def funfactsJson():
	facts = [

		{	"Fun": 			"Number of homes in need of a lawnmower ",
			"data":			funFacts.potentialLandscapingCustomers(),
			"Fun2":			" houses recieved 'Overgrown Yard / Weeds' violations"
		},

		{	"Fun":			"Fowl Play",
			"data":			funFacts.fowlPlay(),
			"Fun2":			" houses recieved 'Fowl or Livestock' violations"
		},

		{	"Fun":			"nlogDead",
			"data":			funFacts.treeSqueezers(),
			"Fun2":			" houses recieved 'Dead or Hazardous Trees' violations"
		},



		{	"Fun":			"The address and quantity of the biggest water waster ",
			"data":			funFacts.maxCityWater(),
			"Fun2":			" "

		},

		{	"Fun":			"The address and quantity of the gassiest in town ",
			"data":			funFacts.maxCityNatGas(),
			"Fun2":			" "
		},

		{	"Fun":			"The address and quantity of the brightest ",
			"data":			funFacts.maxCityElect(),
			"Fun2":			" "

		},

		{	"Fun":			"The average Electricity, Water, and Natural Gas of all address that begin with the number 1",
			"data":			funFacts.avgNumOne(),
			"Fun2":			" "
		},

		{	"Fun":			"The average Electricity, Water, and Natural Gas of all address that begin with the number 3",
			"data":			funFacts.avgNumThree(),
			"Fun2":			" "
		},

		{	"Fun":			"The average Electricity, Water, and Natural Gas of all address that begin with the number 4",
			"data":			funFacts.avgNumFour(),
			"Fun2":			" "
		},

		{	"Fun":			"The average Electricity, Water, and Natural Gas of all address that begin with the number 5",
			"data":			funFacts.avgNumFive(),
			"Fun2":			" "
		},

		{	"Fun":			"The average Electricity, Water, and Natural Gas of all address that begin with the number 6",
			"data":			funFacts.avgNumSix(),
			"Fun2":			" "
		},

		{	"Fun":			"The average Electricity, Water, and Natural Gas of all address that begin with the number 7",
			"data":			funFacts.avgNumSeven(),
			"Fun2":			" "
		},

		{	"Fun":			"The average Electricity, Water, and Natural Gas of all address that begin with the number 8",
			"data":			funFacts.avgNumEight(),
			"Fun2":			" "
		},

		{	"Fun":			"The average Electricity, Water, and Natural Gas of all address that begin with the number 9",
			"data":			funFacts.avgNumNine(),
			"Fun2":			" "
		}


	]

	return json.jsonify({ "facts": facts })


@app.route('/FunFacts/')
def funfactsRend():
	facts = [

		{	"Fun": 			"Number of homes in need of a lawnmower ",
			"data":			funFacts.potentialLandscapingCustomers(),
			"Fun2":			" houses recieved 'Overgrown Yard / Weeds' violations"
		},

		{	"Fun":			"Fowl Play",
			"data":			funFacts.fowlPlay(),
			"Fun2":			" houses recieved 'Fowl or Livestock' violations"
		},

		{	"Fun":			"nlogDead",
			"data":			funFacts.treeSqueezers(),
			"Fun2":			" houses recieved 'Dead or Hazardous Trees' violations"
		},


		{	"Fun":			"The address and quantity of the biggest water waster ",
			"data":			funFacts.maxCityWater(),
			"Fun2":			" "

		},

		{	"Fun":			"The address and quantity of the gassiest in town ",
			"data":			funFacts.maxCityNatGas(),
			"Fun2":			" "
		},

		{	"Fun":			"The address and quantity of the brightest ",
			"data":			funFacts.maxCityElect(),
			"Fun2":			" "

		},

		{	"Fun":			"The average Electricity, Water, and Natural Gas of all address that begin with the number 1",
			"data":			funFacts.avgNumOne(),
			"Fun2":			" "
		},

		{	"Fun":			"The average Electricity, Water, and Natural Gas of all address that begin with the number 3",
			"data":			funFacts.avgNumThree(),
			"Fun2":			" "
		},

		{	"Fun":			"The average Electricity, Water, and Natural Gas of all address that begin with the number 4",
			"data":			funFacts.avgNumFour(),
			"Fun2":			" "
		},

		{	"Fun":			"The average Electricity, Water, and Natural Gas of all address that begin with the number 5",
			"data":			funFacts.avgNumFive(),
			"Fun2":			" "
		},

		{	"Fun":			"The average Electricity, Water, and Natural Gas of all address that begin with the number 6",
			"data":			funFacts.avgNumSix(),
			"Fun2":			" "
		},

		{	"Fun":			"The average Electricity, Water, and Natural Gas of all address that begin with the number 7",
			"data":			funFacts.avgNumSeven(),
			"Fun2":			" "
		},

		{	"Fun":			"The average Electricity, Water, and Natural Gas of all address that begin with the number 8",
			"data":			funFacts.avgNumEight(),
			"Fun2":			" "
		},

		{	"Fun":			"The average Electricity, Water, and Natural Gas of all address that begin with the number 9",
			"data":			funFacts.avgNumNine(),
			"Fun2":			" "
		}

	]

	return render_template('FunFacts.html', facts = facts )

@app.route('/TUPLES')
def totalTuples():
	return json.jsonify({"totalTuples": totaltuples.totalTuples()})