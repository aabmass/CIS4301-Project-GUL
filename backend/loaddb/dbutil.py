#!/usr/bin/env python2

import json
import sys
import cx_Oracle as oracle

con = None
cur = None

def getCursor():
    global con
    global cur

    if con is None:
        if (len(sys.argv) == 2):
            # SSH port forwarding is done, use localhost
            con = oracle.connect("aaron/itsmeaa1@localhost/orcl")
        else:
            # We are running on UF domain, connect to oracle.ci...
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
