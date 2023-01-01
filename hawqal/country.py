from dal.dao import Database
from filter.filter import Filter
import os
import string


class Country:
    """
    1. Countries function takes two parameters as input country name and filters.\n
    2. By default, function will return countries name.\n
    3. Additional fields are included in filter.\n
    4. From filter of boolean TRUE fields will be included in output
        e.g
            {
                "coordinates": True,
                "region": True,
                "currency": True,
                "timezone": True,
                "capital": True
            }

    """

    @staticmethod
    def getCountries(country="", meta={}):
        dirname = os.path.dirname(__file__)
        file_name = os.path.join(dirname, '..', 'database', 'hawqalDB.sqlite')
        with open(file_name, 'r', encoding="utf8") as db:
            database = Database(file_name).makeConnection()
            cursor = database.cursor()
        if country == "" and len(meta) == 0:
            data = cursor.execute(
                f"SELECT country_name FROM countries ORDER BY country_name ASC")
            return [country[0] for country in list(data)]
        elif type(country) == type({}):
            if type(meta) == type(""):
                if meta != "":
                    selectedFields = Filter.CountryFilter(country)
                    meta = string.capwords(meta)
                    data = cursor.execute(
                        f'SELECT country_name,{selectedFields} FROM countries WHERE country_name = "{meta}"')
                    return [list(country) for country in data][0]
                else:
                    selectedFields = Filter.CountryFilter(country)
                    data = cursor.execute(
                        f'SELECT country_name,{selectedFields} FROM countries')
                    return [list(country) for country in data]
            else:
                meta, country = country, ""
                selectedFields = Filter.CountryFilter(meta)
                data = cursor.execute(
                    f'SELECT country_name,{selectedFields} FROM countries')
                return [list(country) for country in data]
        elif (country != "" and len(meta) > 0):
            country = string.capwords(country)
            selectedFields = Filter.CountryFilter(meta)
            data = cursor.execute(
                f'SELECT country_name,{selectedFields} FROM countries WHERE country_name = "{country}"')
            return [list(country) for country in data][0]
        elif (country != "" and len(meta) == 0):
            country = string.capwords(country)
            data = cursor.execute(
                f'SELECT * FROM countries WHERE country_name = "{country}"')
            return [list(country) for country in data][0]
