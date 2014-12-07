#!/usr/bin/env python2
import sys
sys.path.append("../")

from loaddb import dbutil

def findElectricity(addrs):
    return dbutil.runSQLAsDict("""SELECT Consumption from ELECTRICITYREPORT, Address Where
 Address.ID = ELECTRICITYREPORT.ADDRESS_ID AND
 Address.StreetAddress = {}""".format( '\'' + addrs + '\''))

def streetElectricity(addrs):

	newAddrs = addrs.split(' ', 1)

	return dbutil.runSQLAsDict("""SELECT AVG(Consumption) from ELECTRICITYREPORT, Address Where
		Address.ID = ElectricityReport.ADDRESS_ID and 
		Address.StreetAddress LIKE {}""".format('\'' + '% ' + newAddrs[1] + '\''))

#class ElectricityReport(object):
#    def __init__(self, id, address_Id, month,
#                 year, consumption):
#        self.id = id
#        self.address_Id=address_Id
#        self.month = month
#        self.year = year
#        self.consumption = consumption
