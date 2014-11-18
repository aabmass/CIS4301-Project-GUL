#!/usr/bin/env python2
import json
import dbutil

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


class Gas:
    def __init__(self):
        # The data as a dictionary
        self.data = JSONData('/home/aaron/Downloads/naturalgas.json')
        print self.data.getRows()[0]

    def insertIntoDatabase(self):
        cur = dbutil.getCursor()
        queryString = """
        INSERT INTO ElectricityReport VALUES(
            :ID, :address_ID, :month, :year, :consumption
        )
        """
        #cur.execute(queryString, ID=

gas = Gas()


# print pprint(getColumns('/home/aaron/Downloads/electricity.json'))
