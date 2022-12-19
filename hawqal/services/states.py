from hawqal.dal.dao import Database


class State:

    @staticmethod
    def getStates():
        states = []
        file_name = "database/hawqalDB.sqlite"
        with open(file_name, 'r', encoding="utf8") as db:
            database = Database(file_name).makeConnection()
            cursor = database.cursor()
            data = cursor.execute(
                "SELECT * FROM states ORDER BY name ASC")
            for row in data:
                states.append([row[1], row[3]])
        return states
