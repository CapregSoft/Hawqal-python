from dal.dao import Database
from .filters.filter import Filter
from Json.Query import convertJson
from .filters.country_filter import CountryFilter
import string
import os


class Country:

    @staticmethod
    def getCountries(filter=CountryFilter()):
        """
            1. Countries function takes two parameters as input country name and meta.\n
            2. By default, function will return countries name.\n
            3. Additional fields are included in filter.\n
            4. From meta TRUE fields will be included in output
                e.g
                    {
                        "coordinates": True,
                        "region": True,
                        "currency": True,
                        "timezone": True,
                        "capital": True
                    }

        """
        file_name = os.path.join(
            os.path.dirname(__file__), '..', 'database', 'hawqalDB.sqlite')

        with open(file_name, 'r', encoding="utf8") as db:
            database = Database(file_name).makeConnection()
            cursor = database.cursor()

        query = "SELECT " + str(filter)

        query = query + " FROM countries ORDER BY country_name ASC"
        print(query)
        cursor.execute(query)

        return convertJson(cursor)

    @staticmethod
    def getCountry(country_name="", filter=CountryFilter()):
        """
            1. Countries function takes two parameters as input country name and meta.\n
            2. By default, function will return countries name.\n
            3. Additional fields are included in filter.\n
            4. From meta TRUE fields will be included in output
                e.g
                    {
                        "coordinates": True,
                        "region": True,
                        "currency": True,
                        "timezone": True,
                        "capital": True
                    }

        """
        file_name = os.path.join(
            os.path.dirname(__file__), '..', 'database', 'hawqalDB.sqlite')

        with open(file_name, 'r', encoding="utf8") as db:
            database = Database(file_name).makeConnection()
            cursor = database.cursor()

        if country_name == "":
            raise ValueError("country_name must be set")

        query = "SELECT " + str(filter) + " FROM countries"

        if country_name != "":

            query = query + \
                f" WHERE country_name = '{string.capwords(country_name)}' ORDER BY country_name ASC"

        cursor.execute(query)

        return convertJson(cursor)
