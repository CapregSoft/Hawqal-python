from dal.dao import Database
import string
import os


class City:

    @staticmethod
    def getCities(country="", state=""):
        country = string.capwords(country)
        state = string.capwords(state)
        cities = []
        dirname = os.path.dirname(__file__)
        file_name = os.path.join(
            dirname, '..', 'database', 'hawqalDB.sqlite')
        with open(file_name, 'r', encoding="utf8") as db:
            database = Database(file_name).makeConnection()
            cursor = database.cursor()
        if state == "" and country == "":
            data = cursor.execute(
                f"SELECT city_name FROM cities ORDER BY city_name")
            for city in list(data):
                cities.append(*city)
            return cities
        elif country != "" and state == "":
            data = cursor.execute(
                f"SELECT city_name FROM cities WHERE country_name = '{country}'")
            for city in list(data):
                cities.append(*city)
            return cities
        elif country == "" and state != "":
            data = cursor.execute(
                f"SELECT cities.city_name FROM cities,states WHERE cities.state_id == states.state_id AND states.state_name == '{state}'")
            return [city for city in data]
