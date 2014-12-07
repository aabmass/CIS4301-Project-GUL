#!/usr/bin/env python2
import sys
sys.path.append("../")

from loaddb import dbutil

def findOneByID(id):
    return dbutil.runSQLAsDict("""SELECT * FROM ADDRESS WHERE
                               ADDRESS.ID = {}""".format(id))


def findElectricity(addrs):
    return dbutil.runSQLAsDict(""" SELECT CONSUMPTION FROM ELECTRICITYREPORT, ADDRESS WHERE
                                ADDRESS.STREETADDRESSS = {} AND 
                                WHERE ADDRESS.ID = ELECTRICITYREPORT.ADDRESS_ID""".format(addrs))

class Address(object):
    def __init__(self, id, streetAddress, city,
                 coord_Lat, coord_Lon):
        self.id = id
        self.streetAddress = streetAddress
        self.city = city
        self.coord_Lat = coord_Lat
        self.coord_Lon = coord_Lon

    # Static functions for Country
