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
            if (row['Month'] == 'January' and row['Year'] == '2013'):
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


parser = argparse.ArgumentParser(description='Get filenames')
parser.add_argument('-l', '--local', action='store_true',
                    help='Pass this flag to connect to \'localhost\'')
parser.add_argument('--gas', required=True,
                    help='Path to the gas usage json file')
args = parser.parse_args()

gasData = JSONData(args.gas)
addAndGas = AddressAndGas(gasData)
print "Going to insert Addresses and Gas datas into database..."
addAndGas.insertIntoDatabase()


# print pprint(getColumns('/home/aaron/Downloads/electricity.json'))
