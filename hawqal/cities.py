from dal.dao import Database
import string
import os


class City:

    @staticmethod
    def getCities(country="", state=""):
        dirname = os.path.dirname(__file__)
        file_name = os.path.join(
            dirname, '..', 'database', 'hawqalDB.sqlite')
        if state == "" and country == "":
            cities = []
            with open(file_name, 'r', encoding="utf8") as db:
                database = Database(file_name).makeConnection()
                cursor = database.cursor()
                data = cursor.execute("SELECT name FROM cities ORDER BY name")
                cities = [city[0] for city in data]
            return cities
        elif country != "" and state == "":
            cities = []
            country = string.capwords(country)
            with open(file_name, 'r', encoding="utf8") as db:
                database = Database(file_name).makeConnection()
                cursor = database.cursor()
                data = cursor.execute(
                    f"SELECT name FROM cities WHERE country_name = '{country}'")
                cities = [city[0] for city in data]
            return cities
        elif country == "" and state != "":
            cities = []
            state = string.capwords(state)
            with open(file_name, 'r', encoding="utf8") as db:
                database = Database(file_name).makeConnection()
                cursor = database.cursor()
                data = cursor.execute(
                    f"SELECT cities.name FROM cities,states WHERE cities.state_id == states.state_id AND states.name == '{state}'")
                cities = [city[0] for city in data]
            return cities
        else:
            pass
