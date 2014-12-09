#!/usr/bin/env python2
import sys
sys.path.append("../")

from loaddb import dbutil



def maxCityElect():
	return dbutil.runSQLAsDict("""SELECT streetaddress, consumption 
		from address, electricityreport 
		where ( select Max(Consumption) from electricityreport) = electricityreport.consumption AND 
		address.id = electricityreport.address_id""")

def maxCityWater():
	return dbutil.runSQLAsDict("""SELECT streetaddress, consumption 
		from address, waterreport 
		where ( select Max(Consumption) from waterreport) = waterreport.consumption AND 
		address.id = waterreport.address_id""")

def maxCityNatGas():
	return dbutil.runSQLAsDict("""SELECT streetaddress, consumption 
		from address, naturalgasreport 
		where ( select Max(Consumption) from naturalgasreport) = naturalgasreport.consumption AND 
		address.id = naturalgasreport.address_id""")


def potentialLandscapingCustomers():
	return dbutil.runSQLAsDict("""SELECT Count(violation) as LawnsInNeed from codeviolationsreport 
		where violation = 'Overgrown Yard / Weeds'""")

def fowlPlay():
	return dbutil.runSQLAsDict("""SELECT count(id) as  from CODEVIOLATIONSREPORT 
		where VIOLATION = 'Fowl or Livestock Prohibited'""")

def treeSqueezers():
	return dbutil.runSQLAsDict("""SELECT count(id) as  from CODEVIOLATIONSREPORT 
		where VIOLATION = 'Dead or Hazardous Trees'""")


def avgNumOne():
	return dbutil.runSQLAsDict("""SELECT avg(electricityreport.consumption) as ElectAvg, 
       avg(waterreport.consumption) as WaterAvg, 
       avg(naturalgasreport.consumption) as NatGasAvg 
       from ELECTRICITYREPORT, waterreport, address, naturalgasreport
where ELECTRICITYREPORT.ADDRESS_ID = address.id AND 
      Waterreport.address_id = address.id and
      NaturalGasReport.address_id = address.id and 
      address.streetaddress LIKE '1 %'""")


def avgNumThree():
	return dbutil.runSQLAsDict("""SELECT avg(electricityreport.consumption) as ElectAvg, 
       avg(waterreport.consumption) as WaterAvg, 
       avg(naturalgasreport.consumption) as NatGasAvg 
       from ELECTRICITYREPORT, waterreport, address, naturalgasreport
where ELECTRICITYREPORT.ADDRESS_ID = address.id AND 
      Waterreport.address_id = address.id and
      NaturalGasReport.address_id = address.id and 
      address.streetaddress LIKE '3 %'""")

def avgNumFour():
	return dbutil.runSQLAsDict("""SELECT avg(electricityreport.consumption) as ElectAvg, 
       avg(waterreport.consumption) as WaterAvg, 
       avg(naturalgasreport.consumption) as NatGasAvg 
       from ELECTRICITYREPORT, waterreport, address, naturalgasreport
where ELECTRICITYREPORT.ADDRESS_ID = address.id AND 
      Waterreport.address_id = address.id and
      NaturalGasReport.address_id = address.id and 
      address.streetaddress LIKE '4 %'""")

def avgNumFive():
	return dbutil.runSQLAsDict("""SELECT avg(electricityreport.consumption) as ElectAvg, 
       avg(waterreport.consumption) as WaterAvg, 
       avg(naturalgasreport.consumption) as NatGasAvg 
       from ELECTRICITYREPORT, waterreport, address, naturalgasreport
where ELECTRICITYREPORT.ADDRESS_ID = address.id AND 
      Waterreport.address_id = address.id and
      NaturalGasReport.address_id = address.id and 
      address.streetaddress LIKE '5 %'""")

def avgNumSix():
	return dbutil.runSQLAsDict("""SELECT avg(electricityreport.consumption) as ElectAvg, 
       avg(waterreport.consumption) as WaterAvg, 
       avg(naturalgasreport.consumption) as NatGasAvg 
       from ELECTRICITYREPORT, waterreport, address, naturalgasreport
where ELECTRICITYREPORT.ADDRESS_ID = address.id AND 
      Waterreport.address_id = address.id and
      NaturalGasReport.address_id = address.id and 
      address.streetaddress LIKE '6 %'""")

def avgNumSeven():
	return dbutil.runSQLAsDict("""SELECT avg(electricityreport.consumption) as ElectAvg, 
       avg(waterreport.consumption) as WaterAvg, 
       avg(naturalgasreport.consumption) as NatGasAvg 
       from ELECTRICITYREPORT, waterreport, address, naturalgasreport
where ELECTRICITYREPORT.ADDRESS_ID = address.id AND 
      Waterreport.address_id = address.id and
      NaturalGasReport.address_id = address.id and 
      address.streetaddress LIKE '7 %'""")

def avgNumEight():
	return dbutil.runSQLAsDict("""SELECT avg(electricityreport.consumption) as ElectAvg, 
       avg(waterreport.consumption) as WaterAvg, 
       avg(naturalgasreport.consumption) as NatGasAvg 
       from ELECTRICITYREPORT, waterreport, address, naturalgasreport
where ELECTRICITYREPORT.ADDRESS_ID = address.id AND 
      Waterreport.address_id = address.id and
      NaturalGasReport.address_id = address.id and 
      address.streetaddress LIKE '8 %'""")

def avgNumNine():
	return dbutil.runSQLAsDict("""SELECT avg(electricityreport.consumption) as ElectAvg, 
       avg(waterreport.consumption) as WaterAvg, 
       avg(naturalgasreport.consumption) as NatGasAvg 
       from ELECTRICITYREPORT, waterreport, address, naturalgasreport
where ELECTRICITYREPORT.ADDRESS_ID = address.id AND 
      Waterreport.address_id = address.id and
      NaturalGasReport.address_id = address.id and 
      address.streetaddress LIKE '9 %'""")
