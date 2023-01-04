from dal.dao import Database
from filter.filter import Filter
import string
import os


class States:

    @staticmethod
    def getStates(country="", meta={}):
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

        if country == "" and len(meta) == 0:
            data = cursor.execute(
                f'SELECT state_name FROM states')
            return [state[0] for state in data]

        elif country == "" and len(meta) != 0:
            selectedFields = Filter.StateFilter(meta)
            if len(selectedFields) != 0:
                data = cursor.execute(
                    f'SELECT state_name,{selectedFields} FROM states')
                return [list(state) for state in data]
            else:
                data = cursor.execute(
                    f'SELECT state_name FROM states')
                return [state for state in data]

        elif country != "" and len(meta) > 0:
            selectedFields = Filter.StateFilter(meta)
            if len(selectedFields) != 0:
                data = cursor.execute(
                    f'SELECT state_name,{selectedFields} FROM states WHERE country_name = "{string.capwords(country)}"')
                return [list(state) for state in data]
            else:
                data = cursor.execute(
                    f'SELECT state_name FROM states WHERE country_name = "{string.capwords(country)}"')
                return [state[0] for state in data]

        elif country != "" and len(meta) == 0:
            selectedFields = Filter.StateFilter(meta)
            data = cursor.execute(
                f'SELECT state_name FROM states WHERE country_name = "{string.capwords(country)}"')
            return [state[0] for state in list(data)]
