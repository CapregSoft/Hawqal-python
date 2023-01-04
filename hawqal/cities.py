from dal.dao import Database
import string
import os
from .filters.city_filter import CityFilter
from Json.Query import convertJson


class City:

    @staticmethod
    def getCities(country_name="", state_name="", filter=CityFilter()):
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

        query = "SELECT " + str(filter) + " FROM cities"

        if country_name != "":
            query = query + \
                f" WHERE country_name = '{string.capwords(country_name)}'"
        elif state_name != "":
            query = query + \
                f" WHERE state_name = '{string.capwords(state_name)}'"

        cursor.execute(query)

        return convertJson(cursor)

    @staticmethod
    def getCity(country_name="", state_name="", city_name="", filter=CityFilter()):
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
        if country_name == "" or state_name == "" or city_name == "":
            raise ValueError("country,state and city name must be set")

        file_name = os.path.join(
            os.path.dirname(__file__), '..', 'database', 'hawqalDB.sqlite')

        with open(file_name, 'r', encoding="utf8") as db:
            database = Database(file_name).makeConnection()
            cursor = database.cursor()

        query = "SELECT " + \
            str(filter) + \
            f" FROM cities WHERE country_name='{string.capwords(country_name)}' AND state_name='{string.capwords(state_name)}' AND city_name = '{string.capwords(city_name)}'"

        cursor.execute(query)

        return convertJson(cursor)
