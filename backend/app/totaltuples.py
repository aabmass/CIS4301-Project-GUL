#!/usr/bin/env python2
import sys
sys.path.append("../")

from loaddb import dbutil


def totalTuples():

	totAddress = dbutil.runSQLAsDict("""SELECT Count(ID) from address""")
	print('\n\n' + totAddress + '\n\n\n\n')
	totElect = dbutil.runSQLAsDict("""SELECT Count(ID) from Electricityreport""")
	print(totElect)
	totNatGas = dbutil.runSQLAsDict("""SELECT Count(ID) from NaturalGasReport""")
	print(totNatGas)
	totCodeVio = dbutil.runSQLAsDict("""SELECT Count(ID) from CodeViolationsReport""")
	totWater = dbutil.runSQLAsDict("""SELECT Count(ID) from WaterReport""")

	total = totAddress + totElect + totNatGas + totWater



	return 