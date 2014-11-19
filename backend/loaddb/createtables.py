#!/usr/bin/env python2

from dbutil import *

def createTables():
    """ Populate the array with names of sql DDL files """
    for sqlFileName in ["Address.sql", "Electricity.sql", "CodeViolationsReport.sql",
                        "FireRescueEMSResponse.sql", "NaturalGasReport.sql"]:
        try:
            runSqlFile("create/" + sqlFileName)  
            print "Created table '{}'".format(sqlFileName.split(".sql")[0])
        except Exception as e:
            pass

createTables()
