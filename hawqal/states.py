from dal.dao import Database
import string
import os


class States:

    @staticmethod
    def getStates(country=""):
        if country == "":
            states = []
            dirname = os.path.dirname(__file__)
            file_name = os.path.join(
                dirname, '..', 'database', 'hawqalDB.sqlite')
            with open(file_name, 'r', encoding="utf8") as db:
                database = Database(file_name).makeConnection()
                cursor = database.cursor()
                data = cursor.execute(
                    f'SELECT name FROM states')
                for row in data:
                    states.append(f'{row[0]}')
            return states
        else:
            states = []
            country = string.capwords(country)
            dirname = os.path.dirname(__file__)
            file_name = os.path.join(
                dirname, '..', 'database', 'hawqalDB.sqlite')
            with open(file_name, 'r', encoding="utf8") as db:
                database = Database(file_name).makeConnection()
                cursor = database.cursor()
                data = cursor.execute(
                    f'SELECT name FROM states WHERE country_name = "{country}"')
                for row in data:
                    states.append(f'{row[0]}')
            return states
