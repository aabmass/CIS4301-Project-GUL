#!/usr/bin/env python2
import sys
sys.path.append("../")

from loaddb import dbutil


def cityAvgWater():
	return dbutil.runSQLAsDict("""SELECT AVG(Consumption) from WaterReport""")

def findWater(addrs):
    return dbutil.runSQLAsDict("""SELECT Consumption from WaterReport, Address Where
 Address.ID = WaterReport.ADDRESS_ID AND
 Address.StreetAddress = {}""".format( '\'' + addrs + '\''))

def streetWater(addrs):

	newAddrs = addrs.split(' ', 1)

	return dbutil.runSQLAsDict("""SELECT AVG(Consumption) from WaterReport, Address Where
		Address.ID = WaterReport.ADDRESS_ID and 
		Address.StreetAddress LIKE {}""".format('\'' + '% ' + newAddrs[1] + '\''))

