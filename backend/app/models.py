from app import app
import cx_Oracle as oracle

def runSQLAsDict(sqlString):
    """ Returns a dictionary for the given sqlString query """
    con = oracle.connect("aaron/itsmeaa1@orcl")
    cur = con.cursor()
    cur.execute(sqlString)

    # Encode it as a python dictionary
    desc = [d[0] for d in cur.description]
    result = [dict(zip(desc,line)) for line in cur]

    cur.close()
    con.close()
    return result

class Address:
    def __init__(self, id, capital, province):
        self.id = id 
        self.capital = capital
        self.province = province

    # Static functions for Country
    @staticmethod
    def findAll():
        return runSQLAsDict("SELECT * FROM ADDRESS")
