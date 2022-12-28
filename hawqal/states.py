from dal.dao import Database
import string
import os


class States:

    @staticmethod
    def getStates(country=""):
        dirname = os.path.dirname(__file__)
        file_name = os.path.join(
            dirname, '..', 'database', 'hawqalDB.sqlite')
        if country == "":
            states = []
            with open(file_name, 'r', encoding="utf8") as db:
                database = Database(file_name).makeConnection()
                cursor = database.cursor()
                data = cursor.execute(
                    'SELECT name FROM states')
                states = [row[0] for row in data]
            return states
        else:
            states = []
            country = string.capwords(country)
            with open(file_name, 'r', encoding="utf8") as db:
                database = Database(file_name).makeConnection()
                cursor = database.cursor()
                data = cursor.execute(
                    f'SELECT name FROM states WHERE country_name = "{country}"')
                states = [row[0] for row in data]
            return states
