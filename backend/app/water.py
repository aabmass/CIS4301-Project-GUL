#!/usr/bin/env python2
import sys
sys.path.append("../")

from loaddb import dbutil


def cityTotalWater():
	x = dbutil.runSQLAsDict("""SELECT SUM(Consumption) as tot from WaterReport""")

	if x:
		return x
	else:
		return "N/A"

def cityAvgWater():
	x = dbutil.runSQLAsDict("""SELECT AVG(Consumption) as avg from WaterReport""")

	if x:
		return x
	else:
		return "N/A"

def findWater(addrs):



    x = dbutil.runSQLAsDict("""SELECT Consumption from WaterReport, Address Where
	 Address.ID = WaterReport.ADDRESS_ID AND
 	 Address.StreetAddress = {}""".format( '\'' + addrs + '\''))

    if x:
	return x
    else: 
    	return "N/A"


def streetWater(addrs):

	newAddrs = addrs.split(' ', 1)

	x = dbutil.runSQLAsDict("""SELECT AVG(Consumption) as avgSt from WaterReport, Address Where
		Address.ID = WaterReport.ADDRESS_ID and 
		Address.StreetAddress LIKE {}""".format('\'' + '% ' + newAddrs[1] + '\''))

	if x:
		return x
	else:
		return "N/A"

