#!/usr/bin/env python2
import sys
sys.path.append("../")

from loaddb import dbutil


def totalTuples():

	totAddress = dbutil.runSQLAsDict("""SELECT Count(ID) from address""")
	totElect = dbutil.runSQLAsDict("""SELECT Count(ID) from Electricityreport""")
	totNatGas = dbutil.runSQLAsDict("""SELECT Count(ID) from NaturalGasReport""")
	totCodeVio = dbutil.runSQLAsDict("""SELECT Count(ID) from CodeViolationsReport""")
	totWater = dbutil.runSQLAsDict("""SELECT Count(ID) from WaterReport""")

	total = totAddress + totElect + totNatGas + totCodeVio + totWater
	numtotal = int(total)

	return numtotal