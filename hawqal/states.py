from dal.dao import Database
import string


class StatesByCountry:

    @staticmethod
    def getStates(country):
        states = []
        country = string.capwords(country)
        file_name = "/hawqal/database/hawqalDB.sqlite"
        with open(file_name, 'r', encoding="utf8") as db:
            database = Database(file_name).makeConnection()
            cursor = database.cursor()
            data = cursor.execute(
                f'SELECT name FROM states WHERE country_name = "{country}"')
            for row in data:
                states.append(f'{row[0]}')
        return states

print(StatesByCountry.getStates("united states"))