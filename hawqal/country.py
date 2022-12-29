from dal.dao import Database
import os
import string


def filterFields(meta):
    fields = ''
    keyArrtibutes = {
        "coordinates": 'latitude,longitude',
        "region": 'region,subregion',
        "currency": 'currency,currency_name,currency_symbol',
        "timezone": 'timezone,zone_city,UTC',
        "capital": 'country_name,country_domain,phone_code,iso_code'
    }
    for key, value in meta.items():
        if value:
            fields = fields + keyArrtibutes[key]+','
    return fields[:-1]


class Country:

    @staticmethod
    def getCountries(country='', meta={}):
        countries = []
        dirname = os.path.dirname(__file__)
        file_name = os.path.join(dirname, '..', 'database', 'hawqalDB.sqlite')
        with open(file_name, 'r', encoding="utf8") as db:
            database = Database(file_name).makeConnection()
            cursor = database.cursor()
        if country == "" and len(meta) == 0:
            data = cursor.execute(
                f"SELECT country_name FROM countries ORDER BY country_name ASC")
            countries = [country[0] for country in list(data)]
            return countries
        elif type(country) == type({}):
            meta, country = country, ""
            selectedFields = filterFields(meta)
            data = cursor.execute(f'SELECT {selectedFields} FROM countries')
            return [list(country) for country in data]
        elif (country != "" and len(meta) > 0):
            country = string.capwords(country)
            selectedFields = filterFields(meta)
            data = cursor.execute(
                f'SELECT {selectedFields} FROM countries WHERE country_name = "{country}"')
            return [country for country in list(data)]
