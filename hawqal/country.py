from dal.dao import Database
import os
import string


class Country:

    @staticmethod
    def getCountries():

        countries = []
        dirname = os.path.dirname(__file__)
        file_name = os.path.join(dirname, '..', 'database', 'hawqalDB.sqlite')
        with open(file_name, 'r', encoding="utf8") as db:
            database = Database(file_name).makeConnection()
            cursor = database.cursor()
            data = cursor.execute(
                f"SELECT * FROM countries ORDER BY country_name ASC")
            for row in data:
                countries.append(f'{row[0]}')
        return countries

    @staticmethod
    def getCurrency(country=""):
        currency = []
        country = string.capwords(country)
        dirname = os.path.dirname(__file__)
        file_name = os.path.join(
            dirname, '..', 'database', 'hawqalDB.sqlite')
        with open(file_name, 'r', encoding="utf8") as db:
            database = Database(file_name).makeConnection()
            cursor = database.cursor()
        if country == "":
            data = cursor.execute(
                f"SELECT country_name,currency,currency_name,currency_symbol FROM countries ORDER BY country_name ASC")
            for row in data:
                currency.append([f"{row[0]}", f"{row[1]}",
                                f"{row[2]}", f"{row[3]}"])
            return currency
        else:
            data = cursor.execute(
                f"SELECT currency,currency_name,currency_symbol FROM countries WHERE country_name = '{country}' ORDER BY country_name ASC")
            for row in data:
                for index, _ in enumerate(row):
                    currency.append(row[index])

            return currency
