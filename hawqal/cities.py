from dal.dao import Database
from filter.filter import Filter
import string
import os


class City:

    @staticmethod
    def getCities(country="", state="", meta={}):
        """
        1. Countries function takes two parameters as input country name and filters.\n
        2. By default, function will return countries name.\n
        3. Additional fields are included in filter.\n
        4. From filter of boolean TRUE fields will be included in output
            e.g
                {
                    "coordinates": True,
                    "country": True,
                    "state":True
                }
        """
        file_name = os.path.join(
            os.path.dirname(__file__), '..', 'database', 'hawqalDB.sqlite')

        with open(file_name, 'r', encoding="utf8") as db:
            database = Database(file_name).makeConnection()
            cursor = database.cursor()

        if state == "" and country == "" and len(meta) == 0:
            data = cursor.execute(
                f"SELECT city_name FROM cities ORDER BY city_name")
            cities = [city[0] for city in data]
            return cities
        elif country != "" and type(country) != type({}) and state == "" and len(meta) == 0:
            data = cursor.execute(
                f"SELECT city_name FROM cities WHERE (country_name='{string.capwords(country)}' OR state_name='{string.capwords(country)}') ORDER BY city_name")
            return [city[0] for city in data]

        elif (type(country) == type({}) and state == "" and len(meta) == 0):
            selectedFields = Filter.CityFilters(country)
            if len(selectedFields) != 0:
                data = cursor.execute(
                    f"SELECT city_name,{selectedFields} FROM cities ORDER BY city_name")
                return [list(city) for city in list(data)]
            else:
                data = cursor.execute(
                    f"SELECT city_name FROM cities ORDER BY city_name")
                return [city[0] for city in list(data)]

        elif country != "" and type(state) == type({}) and len(meta) == 0:
            selectedFields = Filter.CityFilters(state)
            if len(selectedFields) != 0:
                data = cursor.execute(
                    f"SELECT city_name,{selectedFields} FROM cities WHERE (country_name='{string.capwords(country)}' OR state_name='{string.capwords(country)}') ORDER BY city_name")
                return [list(city) for city in list(data)]
            else:
                data = cursor.execute(
                    f"SELECT city_name FROM cities WHERE (country_name='{string.capwords(country)}' OR state_name='{string.capwords(country)}') ORDER BY city_name")
                return [city[0] for city in data]

        elif country != "" and state != "" and len(meta) > 0:
            selectedFields = Filter.CityFilters(meta)
            data = cursor.execute(
                f"SELECT city_name,{selectedFields} FROM cities WHERE country_name='{string.capwords(string.capwords(country))}' AND state_name='{string.capwords(string.capwords(state))}' ORDER BY city_name")
            return [list(city) for city in list(data)]
