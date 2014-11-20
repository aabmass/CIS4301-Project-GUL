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
    def __init__(self, data):
        DatabaseTable.__init__(self, data)

    def insertIntoDatabase(self):
        cur = dbutil.getCursor()
        queryString = """
        INSERT INTO ElectricityReport (ID, address_ID, month, year, consumption)
        VALUES(:1, :2, :3, :4, :5)
        """
        ## Further implement here....
        # tmpRows = []
        # index = 1
        # for row in self.data.getRows():
        #     entryTuple = (index, row['ServiceAddress'], row['ServCity'],
        #                   row['Location 1'][1], row['Location 1'][2])
        #     tmpRows.append(entryTuple)
        #     index = index + 1

        # # put them in the database
        # print "One of the tuples is " + str(tmpRows[0])
        # print "Going to insert {} tuples now".format(len(tmpRows))
        # cur.executemany(queryString, tmpRows)
        # cur.close()

# Lets build addresses from Gas data
class Address(DatabaseTable):
    def __init__(self, data):
        DatabaseTable.__init__(self, data)

    def insertIntoDatabase(self):
        cur = dbutil.getCursor()
        queryString = """
        INSERT INTO ADDRESS (ID, streetAddress, city, coord_Lat, coord_Lon)
        VALUES(:1, :2, :3, :4, :5)
        """
        tmpRows = []
        index = 1
        for row in self.data.getRows():
            if (row['Month'] == 'January' and row['Year'] == '2013'):
                entryTuple = (index, row['ServiceAddress'], row['ServCity'],
                              row['Location 1'][1], row['Location 1'][2])
                tmpRows.append(entryTuple)
                index = index + 1

        # put them in the database
        print "One of the tuples is " + str(tmpRows[0])
        print "Going to insert {} tuples now".format(len(tmpRows))
        cur.executemany(queryString, tmpRows)
        dbutil.closeAndCommit()

add = Address.createFromFile('/tmp/naturalgas.json')
print "Going to insert into database..."
add.insertIntoDatabase()


# print pprint(getColumns('/home/aaron/Downloads/electricity.json'))
