from hawqal.dal.dao import Database


class City:

    @staticmethod
    def getCities():
        cities = []
        file_name = "database/hawqalDB.sqlite"
        with open(file_name, 'r', encoding="utf8") as db:
            database = Database(file_name).makeConnection()
            cursor = database.cursor()
            data = cursor.execute(
                f"SELECT * FROM cities ORDER BY name ASC")
            for row in data:
                cities.append([row[1], row[4]])
        return cities
