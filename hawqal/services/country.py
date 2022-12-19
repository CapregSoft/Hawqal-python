from hawqal.dal.dao import Database


class Country:

    @staticmethod
    def getCountries():
        countries = []
        file_name = "database/hawqalDB.sqlite"
        with open(file_name, 'r', encoding="utf8") as db:
            database = Database(file_name).makeConnection()
            cursor = database.cursor()
            data = cursor.execute(
                f"SELECT * FROM countries ORDER BY country_id ASC")
            for row in data:
                countries.append(f'{row[1]}')
        return countries
