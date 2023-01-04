from dal.dao import Database
from .filters.state_filter import StateFilter
import string
import os


class States:

    @staticmethod
    def getStates(country_name="", filter=StateFilter()):
        """
            1. States function takes two parameters as input state name and filters.\n
            2. By default, function will return states name.\n
            3. Additional fields are included in filter.\n
            4. From filter of boolean TRUE fields will be included in output
                e.g
                    {
                        "coordinates":True
                    }

        """
        file_name = os.path.join(
            os.path.dirname(__file__), '..', 'database', 'hawqalDB.sqlite')

        with open(file_name, 'r', encoding="utf8") as db:
            database = Database(file_name).makeConnection()
            cursor = database.cursor()

        query = "SELECT " + str(filter) + " FROM states"

        if len(country_name) > 0:
            query = query + \
                f' where country_name= "{string.capwords(country_name)}"'

        print(query)
        print(filter)
        cursor.execute(query)

        data_json = []
        header = [i[0] for i in cursor.description]
        data = cursor.fetchall()
        for i in data:
            data_json.append(dict(zip(header, i)))
        return data_json

    @staticmethod
    def getState(country_name="", state_name="", filter=StateFilter()):
        if state_name == "":
            raise ValueError("state_name must be set")

        file_name = os.path.join(
            os.path.dirname(__file__), '..', 'database', 'hawqalDB.sqlite')

        with open(file_name, 'r', encoding="utf8") as db:
            database = Database(file_name).makeConnection()
            cursor = database.cursor()

        query = "SELECT " + filter + " FROM states"

        if len(country_name) > 0 and len(state_name) > 0:
            query = f'where country_name= "{string.capwords(country_name)}" and state_name= "{string.capwords(state_name)}"'
        elif len(country_name) > 0:
            query = query + f'where country_name= "{string.capwords(country_name)}"'
        elif len(state_name) > 0:
            query = query + f'where state_name= "{string.capwords(state_name)}"'

        query = query + " ORDER BY country_name"

        cursor.execute(query)

        data_json = []
        header = [i[0] for i in cursor.description]
        data = cursor.fetchall()
        for i in data:
            data_json.append(dict(zip(header, i)))
        return data_json
