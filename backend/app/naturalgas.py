#!/usr/bin/env python2
import sys
sys.path.append("../")

from loaddb import dbutil

def cityTotalNatGas():
	x = dbutil.runSQLAsDict("""SELECT SUM(Consumption) as tot from NaturalGasReport""")

	if x:
		return x
	else:
		return "N/A"

def cityAvgNatGas():
	x = dbutil.runSQLAsDict("""SELECT AVG(Consumption) as avg from NaturalGasReport""")

	if x:
		return x
	else:
		return "N/A"

def findNatGas(addrs):
    x = dbutil.runSQLAsDict("""SELECT Consumption from NaturalGasReport, Address Where
 Address.ID = NaturalGasReport.ADDRESS_ID AND
 Address.StreetAddress = {}""".format( '\'' + addrs + '\''))

    if x:
		return x
	else:
		return "N/A"

def streetNatGas(addrs):

	newAddrs = addrs.split(' ', 1)

	x = dbutil.runSQLAsDict("""SELECT AVG(Consumption) as avgSt from NaturalGasReport, Address Where
		Address.ID = NaturalGasReport.ADDRESS_ID and 
		Address.StreetAddress LIKE {}""".format('\'' + '% ' + newAddrs[1] + '\''))

	if x:
		return x
	else:
		return "N/A"

class NaturalGasReport(object):
    def __init__(self, id, address_Id, month,
                 year, consumption):
        self.id = id
        self.address_Id=address_Id
        self.month = month
        self.year = year
        self.consumption = consumption
