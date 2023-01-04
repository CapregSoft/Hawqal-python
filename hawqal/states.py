from dal.dao import create_cursor
from .filters.state_filter import StateFilter
import string
from Json.Query import convertJson
import os


class States:

    @staticmethod
    def getStates(country_name="", filters=StateFilter()):
        """
            1. States function takes two parameters as input state name and filters.\n
            2. By default, function will return states name.\n
            3. Additional fields are included in filters.\n
            4. From filter of boolean TRUE fields will be included in output
                e.g
                    {
                        "coordinates":True
                    }

        """
        cursor = create_cursor()

        query = "SELECT " + str(filters) + " FROM states"

        if len(country_name) > 0:
            query = query + \
                f' where country_name= "{string.capwords(country_name)}"'

        cursor.execute(query)

        return convertJson(cursor)

    @staticmethod
    def getState(country_name="", state_name="", filters=StateFilter()):
        if state_name == "":
            raise ValueError("state_name must be set")

        query = "SELECT " + filters + " FROM states"
        cursor=create_cursor()
        if len(country_name) > 0 and len(state_name) > 0:
            query = f'where country_name= "{string.capwords(country_name)}" and state_name= "{string.capwords(state_name)}"'
        elif len(country_name) > 0:
            query = query + \
                f'where country_name= "{string.capwords(country_name)}"'
        elif len(state_name) > 0:
            query = query + \
                f'where state_name= "{string.capwords(state_name)}"'

        query = query + " ORDER BY country_name"

        cursor.execute(query)

        return convertJson(cursor)
