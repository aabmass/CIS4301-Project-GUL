#!/usr/bin/env python2
import sys
sys.path.append("../")

from loaddb import dbutil


def totalTuples():

	totAddress = dbutil.runSQLAsDict("""SELECT Count(ID) as cAd from address""")
	totElect = dbutil.runSQLAsDict("""SELECT Count(ID) as cEl from Electricityreport""")
	totNatGas = dbutil.runSQLAsDict("""SELECT Count(ID) as cNa from NaturalGasReport""")
	totCodeVio = dbutil.runSQLAsDict("""SELECT Count(ID) as cCoVi from CodeViolationsReport""")
	totWater = dbutil.runSQLAsDict("""SELECT Count(ID) as cWa from WaterReport""")

	# total = totAddress[0].cAD + totElect[0].cEL + totNatGas[0].cNA + totWater[0].cWA
	total2 = totAddress + totElect + totNatGas + totCodeVio + totWater


	return total2
