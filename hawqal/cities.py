from dal.dao import Database
from filter.filter import Filter
import string
import os


class City:

    @staticmethod
    def getCities(country="", state="", meta={}):
        country = string.capwords(country)
        state = string.capwords(state)
        cities = []
        dirname = os.path.dirname(__file__)
        file_name = os.path.join(
            dirname, '..', 'database', 'hawqalDB.sqlite')
        with open(file_name, 'r', encoding="utf8") as db:
            database = Database(file_name).makeConnection()
            cursor = database.cursor()
        if state == "" and country == "" and len(meta) == 0:
            data = cursor.execute(
                f"SELECT city_name FROM cities ORDER BY city_name")
            cities = [city[0] for city in data]
            return cities
        elif country != "" and state == "" and len(meta) == 0:
            data = cursor.execute(
                f"SELECT city_name FROM cities WHERE country_name = '{country}'")
            cities = [city[0] for city in data]
            return cities
        elif country == "" and state != "" and len(meta) == 0:
            data = cursor.execute(
                f"SELECT cities.city_name FROM cities,states WHERE cities.state_id == states.state_id AND states.state_name == '{state}'")
            return [city[0] for city in data]
        elif (country != "" and state == "" and len(meta) > 0):
            selectedFields = Filter.CityFilters(meta)
            data = cursor.execute(
                f"SELECT city_name,{selectedFields} FROM cities WHERE country_name = '{country}'")
            cities = [list(city) for city in data]
            return cities
        elif (country == "" and state != "" and len(meta) > 0):
            selectedFields = Filter.CityFilters(meta)
            data = cursor.execute(
                f"SELECT cities.city_name,{selectedFields} FROM cities,states WHERE cities.state_id == states.state_id AND states.state_name == '{state}'")
            return [list(city) for city in list(data)]
