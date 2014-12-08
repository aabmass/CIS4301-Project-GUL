#!/usr/bin/env python2
import sys
sys.path.append("../")

from loaddb import dbutil

def cityTotalWater():
	return dbutil.runSQLAsDict("""SELECT SUM(Consumption) from WaterReport""")

def cityAvgWater():
	return dbutil.runSQLAsDict("""SELECT AVG(Consumption) from WaterReport""")

def findWater(addrs):


    x = dbutil.runSQLAsDict("""SELECT Consumption from WaterReport, Address Where
	 Address.ID = WaterReport.ADDRESS_ID AND
 	 Address.StreetAddress = {}""".format( '\'' + addrs + '\''))

    if x == "[]" 
    	return "Sorry no information available"
    else
    	return x

def streetWater(addrs):

	newAddrs = addrs.split(' ', 1)

	return dbutil.runSQLAsDict("""SELECT AVG(Consumption) from WaterReport, Address Where
		Address.ID = WaterReport.ADDRESS_ID and 
		Address.StreetAddress LIKE {}""".format('\'' + '% ' + newAddrs[1] + '\''))

