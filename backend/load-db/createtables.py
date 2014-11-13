#!/usr/bin/env python

from dbutil import *

def createTables():
    """ Populate the array with names of sql DDL files """
    for sqlFileName in ["ADDRESS.sql"]:
        try:
            runSqlFile("create/" + sqlFileName)  
            print "Created table '{}'".format(sqlFileName.split(".sql")[0])
        except Exception as e:
            pass

createTables()
