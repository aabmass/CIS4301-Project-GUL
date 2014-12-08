#!/usr/bin/env python2
import sys
sys.path.append("../")

from loaddb import dbutil


def totalTuples():

	totAddress = dbutil.runSQLAsDict("""SELECT Count(ID) from address""")
	totElect = dbutil.runSQLAsDict("""SELECT Count(ID) from Electricityreport""")
	totNatGas = dbutil.runSQLAsDict("""SELECT Count(ID) from NaturalGasReport""")
	totCodeVio = dbutil.runSQLAsDict("""SELECT Count(ID) from CodeViolationReport""")
	#totWater = dbutil.runSQLAsDict("""SELECT Count(ID) from WaterReport""")
	return totAddress + totElect + totNatGas + totCodeVio;



str.replace(" ", "%20");
