from dal.dao import Database
import os


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
                "SELECT * FROM countries ORDER BY country_id ASC")
            countries = [row[1] for row in data.fetchall()]
        return countries
