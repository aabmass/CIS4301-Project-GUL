#!/usr/bin/env python2
import sys
sys.path.append("../")

from loaddb import dbutil

def findOneByID(id):
    return dbutil.runSQLAsDict("""SELECT * FROM NATURALGASREPORT WHERE
                               NATURALGASREPORT.ID = {}""".format(id))

class NaturalGasReport(object):
    def __init__(self, id, address_Id, month,
                 year, consumption):
        self.id = id
        self.address_Id=address_Id
        self.month = month
        self.year = year
        self.consumption = consumption
