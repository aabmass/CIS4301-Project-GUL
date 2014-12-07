#!/usr/bin/env python2
import sys
sys.path.append("../")

from loaddb import dbutil


def cityAvgNatGas():
	return dbutil.runSQLAsDict("""SELECT AVG(Consumption) from NaturalGasReport""")

def findNatGas(addrs):
    return dbutil.runSQLAsDict("""SELECT Consumption from NaturalGasReport, Address Where
 Address.ID = NaturalGasReport.ADDRESS_ID AND
 Address.StreetAddress = {}""".format( '\'' + addrs + '\''))

def streetNatGas(addrs):

	newAddrs = addrs.split(' ', 1)

	return dbutil.runSQLAsDict("""SELECT AVG(Consumption) from NaturalGasReport, Address Where
		Address.ID = NaturalGasReport.ADDRESS_ID and 
		Address.StreetAddress LIKE {}""".format('\'' + '% ' + newAddrs[1] + '\''))

class NaturalGasReport(object):
    def __init__(self, id, address_Id, month,
                 year, consumption):
        self.id = id
        self.address_Id=address_Id
        self.month = month
        self.year = year
        self.consumption = consumption
