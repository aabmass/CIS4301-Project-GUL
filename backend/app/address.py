#!/usr/bin/env python2
import sys
sys.path.append("../")

from loaddb import dbutil

def findOneByID(id):
    return dbutil.runSQLAsDict("""SELECT * FROM ADDRESS WHERE
                               ADDRESS.ID = {}""".format(id))

def getId(addrs):
    return dbutil.runSQLAsDict("""SELECT ADDRESS.ID FROM ADDRESS WHERE
				ADDRESS.StreetAddress = {}""".format( '\''+ addrs+'\''))

def getInfo(addrs):
    return dbutil.runSQLAsDict("""SELECT id, Streetaddress, coord_lat, coord_lon from ADDRESS
Where streetaddress = {}""".format( '\''+ addrs+'\''))

#class Address(object):
#    def __init__(self, id, streetAddress, city,
#                 coord_Lat, coord_Lon):
#        self.id = id
#        self.streetAddress = streetAddress
#        self.city = city
#        self.coord_Lat = coord_Lat
#        self.coord_Lon = coord_Lon

    # Static functions for Country
