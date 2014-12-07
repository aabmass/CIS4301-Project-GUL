#!/usr/bin/env python2
import sys
sys.path.append("../")

from loaddb import dbutil

def findElectricity(addrs):
    return dbutil.runSQLAsDict(""" SELECT CONSUMPTION FROM ELECTRICITYREPORT, ADDRESS WHERE
                                ADDRESS.STREETADDRESSS = {} AND 
                                WHERE ADDRESS.ID = ELECTRICITYREPORT.ADDRESS_ID""".format(addrs))

class ElectricityReport(object):
    def __init__(self, id, address_Id, month,
                 year, consumption):
        self.id = id
        self.address_Id=address_Id
        self.month = month
        self.year = year
        self.consumption = consumption
