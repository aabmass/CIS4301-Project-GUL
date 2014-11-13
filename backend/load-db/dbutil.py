#!/usr/bin/env python

import json
import cx_Oracle as oracle

con = None
cur = None

def getCursor():
    global con
    global cur
    if con is None:
        con = oracle.connect("aaron/itsmeaa1@oracle.cise.ufl.edu/orcl")
    if cur is None:
        cur = con.cursor()

    return cur

def close():
    cur.close()
    con.commit()
    con.close()

def runSqlFile(filename):
    cur = getCursor()

    with open(filename, 'r') as sqlFile:
        asString = sqlFile.read()
        cur.execute(asString)

def runSQLAsDict(sqlString):
    """ Returns a dictionary for the given sqlString query """
    cur = getCursor()
    cur.execute(sqlString)

    # Encode it as a python dictionary
    desc = [d[0] for d in cur.description]
    result = [dict(zip(desc,line)) for line in cur]

    con.close()
    return result
