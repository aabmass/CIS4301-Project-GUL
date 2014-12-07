#!/usr/bin/env python2
import sys
sys.path.append("../")

from loaddb import dbutil

def findCodeVio(addrs):
    return dbutil.runSQLAsDict("""SELECT Violation, CaseType, Inspector from CodeViolationsreport, address
								where address.id = CodeViolationsreport.ADDRESS_ID and 
								address.STREETADDRESS = {}""".format( '\'' + addrs + '\''))

def streetCodeVio(addrs):
	return dbutil.runSQLAsDict("""SELECT Violation, CaseType, Inspector from CodeViolationsreport, Address Where
		Address.ID = CodeViolationsreport.ADDRESS_ID and 
		Address.StreetAddress LIKE {}""".format('\'' + '% ' + newAddrs[1] + '\'')))

class CodeViolationsReport(object):
    def __init__(self, id, address_Id, violation,
                 casetype, status):
        self.id = id
        self.address_Id=address_Id
        self.casetype = casetype
        self.inspector = inspector
        self.status = status
