#!/usr/bin/env python2
import sys
sys.path.append("../")

from loaddb import dbutil


def cityTotalElect():
	x = dbutil.runSQLAsDict("""SELECT SUM(Consumption) as tot from ELECTRICITYREPORT""")

	if x:
		return x
	else:
		return "N/A"

def cityAvgElect():
	x = dbutil.runSQLAsDict("""SELECT AVG(Consumption) as avg from ELECTRICITYREPORT""")

	if x:
		return x
	else:
		return "N/A"

def findElectricity(addrs):
    x = dbutil.runSQLAsDict("""SELECT Consumption from ELECTRICITYREPORT, Address Where
 Address.ID = ELECTRICITYREPORT.ADDRESS_ID AND
 Address.StreetAddress = {}""".format( '\'' + addrs + '\''))

    if x:
		return x
	else:
		return "N/A"

def streetElectricity(addrs):

	newAddrs = addrs.split(' ', 1)

	x = dbutil.runSQLAsDict("""SELECT AVG(Consumption) as avgSt from ELECTRICITYREPORT, Address Where
		Address.ID = ElectricityReport.ADDRESS_ID and 
		Address.StreetAddress LIKE {}""".format('\'' + '% ' + newAddrs[1] + '\''))

	if x:
		return x
	else:
		return "N/A"

#class ElectricityReport(object):
#    def __init__(self, id, address_Id, month,
#                 year, consumption):
#        self.id = id
#        self.address_Id=address_Id
#        self.month = month
#        self.year = year
#        self.consumption = consumption
