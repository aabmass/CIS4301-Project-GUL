#!/usr/bin/env python2
import sys
sys.path.append("../")

from loaddb import dbutil


def totalTuples():

	totAddress = int(dbutil.runSQLAsDict("""SELECT Count(ID) from address"""))
	totElect = int(dbutil.runSQLAsDict("""SELECT Count(ID) from Electricityreport"""))
	totNatGas = int(dbutil.runSQLAsDict("""SELECT Count(ID) from NaturalGasReport"""))
	totCodeVio = int(dbutil.runSQLAsDict("""SELECT Count(ID) from CodeViolationsReport"""))
	#totWater = dbutil.runSQLAsDict("""SELECT Count(ID) from WaterReport""")

	total = totAddress + totElect + totNatGas + totCodeVio

	return total