#!/usr/bin/env python2
import json
import dbutil
import sys
import argparse

class JSONData:
    def __init__(self, filename):
        self.filename = filename
        print "Loading data"
        self.loadJSONData()
        print "Loading Columns"
        self.loadColumns()
        print "Loading rows"
        self.loadRows()

    # Returns JSON data as a dictionary for the given json file
    def loadJSONData(self):
        with open(self.filename) as jsonFile:
            self.data = json.load(jsonFile)

    # Data parameter is raw python dictionary
    def loadColumns(self):
        allColumns = self.data['meta']['view']['columns']
        cols = []
        # remove the columns with -1 for ID's

        i = 0
        for col in allColumns:
            if (col['id'] != -1):
                cols.append((i, col['name']))
            i = i + 1
        self.columns = cols

    def loadRows(self):
        self.rows = []
        for entry in self.data['data']:
            newCol = dict()
            for (index, colName) in self.getColumns():
                newCol[colName] = entry[index]
            self.rows.append(newCol)

    # Returns an array of tuples (index, colName)
    def getColumns(self):
        return self.columns

    # Returns an array of dictionaries
    def getRows(self):
        return self.rows

    def setRows(self, newRows):
        self.rows = newRows

    def removeAllRowsNotMatching(self, conditionFunction):
        self.rows[:] = [x for x in self.rows if conditionFunction(x)]

    def removeAllRowsMatching(self, conditionFunction):
        self.rows[:] = [x for x in self.rows if not conditionFunction(x)]

class DatabaseTable(object):
    def __init__(self, data):
        # The data as a dictionary
        self.data = data
        print self.data.getRows()[0]

    @classmethod
    def createFromFile(cls, filename):
        return cls(JSONData(filename))

    def insertIntoDatabase(self):
        raise NotImplementedError("You must override \'insertIntoDatabase\'")

class Gas(DatabaseTable):
    def __init__(self, data, addressTuples):
        DatabaseTable.__init__(self, data)
        self.addressTuples = addressTuples
        self.makeGasTuples()

    def insertIntoDatabase(self):
        cur = dbutil.getCursor()
        queryString = """
        INSERT INTO ElectricityReport (ID, address_ID, month, year, consumption)
        VALUES(:1, :2, :3, :4, :5)
        """

        # index = 1
        # for address in 
        # for row in self.data.getRows():
        #     if (row['Month'] == 'January' and
        #         row['Year'] == '2013' and
        #         ):
        #         entryTuple = (index, row['ServiceAddress'], row['ServCity'],
        #                       row['Location 1'][1], row['Location 1'][2])
        #         self.tuples.append(entryTuple)
        #         index = index + 1

        # cur.executemany(queryString, tmpRows)
        # dbutil.closeAndCommit()

# Lets build addresses from Gas data
class Address(DatabaseTable):
    def __init__(self, data):
        DatabaseTable.__init__(self, data)
        self.makeTuples()

    def makeTuples(self):
        self.tuples = []
        index = 1
        for row in self.data.getRows():
            if (row['Month'] == 'January' and row['Year'] == '2013'):
                entryTuple = (index, row['ServiceAddress'], row['ServCity'],
                              row['Location 1'][1], row['Location 1'][2])
                self.tuples.append(entryTuple)
                index = index + 1

    def insertIntoDatabase(self):
        cur = dbutil.getCursor()
        queryString = """
        INSERT INTO ADDRESS (ID, streetAddress, city, coord_Lat, coord_Lon)
        VALUES(:1, :2, :3, :4, :5)
        """

        # put them in the database
        print "One of the tuples is " + str(self.tuples[0])
        print "Going to insert {} tuples now".format(len(self.tuples))
        cur.executemany(queryString, self.tuples)
        dbutil.closeAndCommit()

class AddressAndGas(DatabaseTable):
    def __init__(self, data):
        DatabaseTable.__init__(self, data)

        # First lets sort self.data.getRows() for later
        print "Sorting rows"
        self.data.getRows().sort(key=lambda row: row['ServiceAddress'])
        self.makeTuples()

    def makeTuples(self):
        self.addressTuples = []
        self.gasTuples = []
        # Address and Gas will have the same indices
        index = 1

        for row in self.data.getRows():
            # Skip rows with no usage
            if (row['Therm Consumption'] is None):
                continue
            elif (row['Month'] == 'January' and row['Year'] == '2013'):
                addressTuple = (index, row['ServiceAddress'], row['ServCity'],
                               row['Location 1'][1], row['Location 1'][2])

                gasTuple = (index, index, row['Month'],
                           row['Year'], row['Therm Consumption'])
                self.addressTuples.append(addressTuple)
                self.gasTuples.append(gasTuple)
                index = index + 1

    def insertIntoDatabase(self):
        cur = dbutil.getCursor()
        addressQueryString = """
        INSERT INTO ADDRESS (ID, streetAddress, city, coord_Lat, coord_Lon)
        VALUES(:1, :2, :3, :4, :5)
        """

        gasQueryString = """
        INSERT INTO NATURALGASREPORT (ID, address_ID, month, year, consumption)
        VALUES(:1, :2, :3, :4, :5)
        """

        # put them in the database
        for (queryString, tuples) in [(addressQueryString, self.addressTuples),
                                      (gasQueryString, self.gasTuples)]:
            print "One of the tuples is " + str(tuples[0])
            print "Going to insert {} tuples now".format(len(tuples))
            cur.executemany(queryString, tuples)
        dbutil.closeAndCommit()


class Electricity(DatabaseTable):
    def __init__(self, data, addressTuples):
        DatabaseTable.__init__(self, data)
        self.addressTuples = addressTuples

        # Lets sort this so our O(n^2) algorithm will be faster
        print "Sorting rows"
        self.data.getRows().sort(key=lambda row: row['ServiceAddress'])
        
        # Lets remove all entries not in January 2013 now
        print "Going to remove all extraneous rows from Electricity"
        before = len(self.data.getRows())

        allAddresses = [x[1] for x in self.addressTuples]
        self.data.removeAllRowsNotMatching(lambda x, addresses=allAddresses:
                x['Month'] == 'January' and x['Year'] == '2013' and
                x['ServiceAddress'] in addresses
            )

        print "Before: {}, After: {}. Going to make tuples".format(before, len(self.data.getRows()))
        self.makeTuples()

    def makeTuples(self):
        self.electricityTuples = []

        index = 1
        for addrTup in self.addressTuples:
            # Lets remove elements from self.data.getRows as they are added
            matchFoundIndex = 0
            for iElec, elecRow in enumerate(self.data.getRows()):
                if (elecRow['KWH Consumption'] == None):
                    continue
                elif (addrTup[1] == elecRow['ServiceAddress']):
                    elecTuple = (index, addrTup[0], elecRow['Month'],
                                 elecRow['Year'], elecRow['KWH Consumption'])
                    self.electricityTuples.append(elecTuple)
                    index = index + 1
                    matchFoundIndex = iElec
                    break;
            if matchFoundIndex != 0:
                self.data.getRows().pop(matchFoundIndex)
                matchFoundIndex = 0

    def insertIntoDatabase(self):
        cur = dbutil.getCursor()

        electricityQueryString = """
        INSERT INTO ELECTRICITYREPORT (ID, address_ID, month, year, consumption)
        VALUES(:1, :2, :3, :4, :5)
        """

        # put them in the database
        print "One of the tuples is " + str(self.electricityTuples[0])
        print "Going to insert {} tuples now".format(len(self.electricityTuples))
        cur.executemany(electricityQueryString, self.electricityTuples)
        dbutil.closeAndCommit()

class CodeViolations(DatabaseTable):
    def __init__(self, data, addressTuples):
        DatabaseTable.__init__(self, data)
        self.addressTuples = addressTuples

        print "Going to remove all extraneous rows from CodeViolations"

        self.data.setRows([row for row in self.data.getRows() if row['Address'] is not None])

        before = len(self.data.getRows())

        allAddresses = [x[1] for x in self.addressTuples]
        self.data.removeAllRowsNotMatching(lambda row, addresses=allAddresses:
                row['Address'].strip("0") in addresses
            )

        print "Before: {}, After: {}. Going to make tuples".format(before, len(self.data.getRows()))

        # Lets sort this so our O(n^2) algorithm will be faster
        print "Sorting rows"
        self.data.getRows().sort(key=lambda row: row['Address'].strip("0"))

        self.makeTuples()

    def makeTuples(self):
        self.codeViolationsTuples = []

        index = 1
        for iAddr, addrTup in enumerate(self.addressTuples):
            # Lets remove elements from self.data.getRows as they are added
            matchFoundIndex = 0
            for iCodeViolation, codeVioRow in enumerate(self.data.getRows()):
                if (codeVioRow['Address'] == None):
                    continue
                #print "addrTup: {}\ncodeVioRow:{}".format(addrTup[1], codeVioRow['Address'].strip())
                elif (addrTup[1] == codeVioRow['Address'].strip("0")):
                    codeVioTuple = (index, addrTup[0], codeVioRow['Violation'],
                                    codeVioRow['Case Type'], codeVioRow['Inspector'],
                                    codeVioRow['Status'])
                    self.codeViolationsTuples.append(codeVioTuple)
                    print index
                    index = index + 1
                    matchFoundIndex = iCodeViolation
                    break;
            if matchFoundIndex != 0:
                self.data.getRows().pop(matchFoundIndex)
                matchFoundIndex = 0

    def insertIntoDatabase(self):
        cur = dbutil.getCursor()

        codeViolationsQueryString = """
        INSERT INTO CODEVIOLATIONSREPORT (ID, address_ID, violation, caseType, inspector, status)
        VALUES(:1, :2, :3, :4, :5, :6)
        """

        # put them in the database
        print "One of the tuples is " + str(self.codeViolationsTuples[0])
        print "Going to insert {} tuples now".format(len(self.codeViolationsTuples[0]))
        cur.executemany(codeViolationsQueryString, self.codeViolationsTuples)
        dbutil.closeAndCommit()

class FireRescue(DatabaseTable):
    def __init__(self, data, addressTuples):
        DatabaseTable.__init__(self, data)
        self.addressTuples = addressTuples

        self.data.setRows([row for row in self.data.getRows() if row['Location 1']['address'] is not None])

        # Lets sort this so our O(n^2) algorithm will be faster
        print "Sorting rows"
        self.data.getRows().sort(key=lambda row: row['Location 1']['address'])
        
        # Lets remove all entries not in January 2013 now
        # print "Going to remove all extraneous rows from CodeViolations"
        # before = len(self.data.getRows())

        # allAddresses = [x[1] for x in self.addressTuples]
        # self.data.removeAllRowsNotMatching(lambda x, addresses=allAddresses:
        #         x['Month'] == 'January' and x['Year'] == '2013' and
        #         x['ServiceAddress'] in addresses
        #     )

        # print "Before: {}, After: {}. Going to make tuples".format(before, len(self.data.getRows()))
        self.makeTuples()

    def makeTuples(self):
        self.tuples = []

        index = 1
        for addrTup in self.addressTuples:
            # Lets remove elements from self.data.getRows as they are added
            matchFoundIndex = 0
            for iFireRescue, fireRescueRow in enumerate(self.data.getRows()):
                address = row['Location 1']['address'].upper()
                if (address is None):
                    continue
                # print "addrTup: {}\nfireRescueRow:{}".format(addrTup[1], fireRescueRow['Address'].strip())
                elif (addrTup[1] == address):
                    fireRescueTuple = (index, addrTup[0], fireRescueRow['Response_Date'],
                                    fireRescueRow['Call Type'], fireRescueRow['Unit'])
                    self.tuples.append(fireRescueTuple)
                    print index
                    index = index + 1
                    matchFoundIndex = iFireRescue
                    break
            if matchFoundIndex != 0:
                self.data.getRows().pop(matchFoundIndex)
                matchFoundIndex = 0

    def insertIntoDatabase(self):
        cur = dbutil.getCursor()

        fireRescueQueryString = """
        INSERT INTO FIRERESCUEEMSRESPONSE (ID, address_ID, responseDate, callType, responseUnit)
        VALUES(:1, :2, :3, :4, :5)
        """

        # put them in the database
        print "One of the tuples is " + str(self.tuples[0])
        print "Going to insert {} tuples now".format(len(self.tuples[0]))
        cur.executemany(fireRescueQueryString, self.tuples)
        dbutil.closeAndCommit()


parser = argparse.ArgumentParser(description='Get filenames')

# Required variables
parser.add_argument('-l', '--local', action='store_true',
                    help='Pass this flag to connect to \'localhost\'')
parser.add_argument('--gas', required=True,
                    help='Path to the gas usage json file')
parser.add_argument('--electricity', required=True,
                    help='Path to the electricity usage json file')
parser.add_argument('--codevio', required=True,
                    help='Path to the code violations json file')
parser.add_argument('--firerescue', required=True,
                    help='Path to the fire rescue/ems json file')

# Optional variables
parser.add_argument('--skipGasAndAddrAndElec', action='store_true',
                    help='Pass this flag to skip gas and electricity tables')

args = parser.parse_args()

gasData = JSONData(args.gas)
addAndGas = AddressAndGas(gasData)
if (not args.skipGasAndAddrAndElec):
    print "Going to insert Addresses and Gas datas into database..."
    addAndGas.insertIntoDatabase()

print "\nNow starting on electricity"
elecData = JSONData(args.electricity)
elec = Electricity(elecData, addAndGas.addressTuples)
elec.insertIntoDatabase()

# codeVioData = JSONData(args.codevio)
# codeVio = CodeViolations(codeVioData, addAndGas.addressTuples)
# codeVio.insertIntoDatabase()

fireRescueData = JSONData(args.firerescue)
fireRescue = FireRescue(fireRescueData, addAndGas.addressTuples)
