from dal.dao import Database
import string
import os


class City:

    @staticmethod
    def getCities(country, state):
        cities = []
        country = string.capwords(country)
        state = string.capwords(state)
        dirname = os.path.dirname(__file__)
        file_name = os.path.join(dirname, '..', 'database', 'hawqalDB.sqlite')
        with open(file_name, 'r', encoding="utf8") as db:
            database = Database(file_name).makeConnection()
            cursor = database.cursor()
            data = cursor.execute(
                f"SELECT cities.name FROM cities,states WHERE cities.state_id=states.state_id AND states.name = '{state}' AND states.country_name = '{country}'")
            for row in data:
                cities.append([row[0]])
        return cities
