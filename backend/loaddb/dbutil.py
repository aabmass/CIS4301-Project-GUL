#!/usr/bin/env python2

import sys
import cx_Oracle as oracle

# Holds the connection in its namespace
class DBUtil(object):
    con = None

def getCursor():
    if DBUtil.con is None:
        if ('--local' in sys.argv):
            # SSH port forwarding is done, use localhost
            DBUtil.con = oracle.connect("aaron/ppppppp@localhost/orcl")
        else:
            # We are running on UF domain, connect to oracle.ci...
            DBUtil.con = oracle.connect("aaron/ppppppp@oracle.cise.ufl.edu/orcl")
    return DBUtil.con.cursor()

def close():
    print "Going to close database"
    DBUtil.con.close()
    DBUtil.con = None

def closeAndCommit():
    print "Commiting to database"
    DBUtil.con.commit()
    close()

def runSqlFile(filename):
    cur = getCursor()

    with open(filename, 'r') as sqlFile:
        asString = sqlFile.read()
        cur.execute(asString)
    cur.close()

def runSQLAsDict(sqlString):
    # Returns a dictionary for the given sqlString query
    cur = getCursor()
    cur.execute(sqlString)

    # Encode it as a python dictionary
    desc = [d[0] for d in cur.description]
    result = [dict(zip(desc, line)) for line in cur]

    cur.close()
    # Don't call close() unless we don't want persistent connection
    return result
