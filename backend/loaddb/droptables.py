#!/usr/bin/env python2
from dbutil import *

def createTables():
    """ Populate the array with names of sql DDL files """
    for table in ["WATERREPORT", "NATURALGASREPORT",
                  "FIRERESCUEEMSRESPONSE", "ELECTRICITYREPORT",
                  "CODEVIOLATIONSREPORT", "ADDRESS"]:
        cur = getCursor()
        cur.execute("DROP TABLE {}".format(table))
        print "Dropped table '{}'".format(table)

createTables()
