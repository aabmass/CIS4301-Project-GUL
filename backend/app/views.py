from app import address
from app import naturalgas
from app import app
from flask import json
from flask import render_template

# Sets up the routes, really

@app.route('/')
def main():
	return render_template('../../index.html')

@app.route('/house/')
def houseNoAddress():
	return render_template('../../house.html')

@app.route('/')
def main():
	return render_template('../../index.html')

@app.route('/house/')
def houseNoAddress():
	return render_template('../../house.html')
	
@app.route('/address/<id>')
def addressId(id):
    return json.jsonify({"addresses": address.findOneByID(id)})

@app.route('/naturalgas/<id>')
def naturalGasId(id):
    return json.jsonify({"naturalgas": naturalgas.findOneByID(id)})
