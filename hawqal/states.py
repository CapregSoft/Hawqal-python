from dal.dao import databaseConnection
from .filters.state_filter import StateFilter
import string
from Json.Query import convertJson
import os


class States:

    @staticmethod
    def getStates(country_name="", filter=StateFilter()):
        """
        Description:\n
            Get information about multiple states from the database
        Default: \n
            By default, this method returns data about all states, including the following fields:\n
            - state_id\n
            - state_name\n
            - country_name\n
            - latitude\n
            - longitude\n
        Args:\n
            filters (StateFilter): Optional : A class object specifying which fields to include in the results.\n
            country_name: Optional : Name of country
        Returns:\n
            list: A JSON object containing the requested information about the countries.\n
        Example: \n
            - To get all the states
                ```
                hawqal.getState()
                ```\n
            - To get state of specific country
                ```
                hawqal.getState(country_name="pakistan",state_name="punjab")
                ```\n
            - To apply filters and exclude longitude
                ```
                hawqal.getState(state_name="punjab",filter=hawqal.StateFilter(longitude=False))
                ```\n
        """
        cursor = databaseConnection()

        query = "SELECT " + str(filter) + " FROM states"

        if len(country_name) > 0:
            query = query + \
                    f' where country_name= "{string.capwords(country_name)}"'

        cursor.execute(query)

        return convertJson(cursor)

    @staticmethod
    def getState(country_name="", state_name="", filter=StateFilter()):
        """
        Description:\n
                Get information about state from the database\n
        Default:
            By default, this method returns data about single state, including the following fields:\n
            - state_id\n
            - state_name\n
            - country_name\n
            - latitude\n
            - longitude\n
        Args:\n
            filters (StateFilter): Optional : A class object specifying which fields to include in the results.\n
            country_name: Optional : Name of country
            state_name: Required : Name of the State
        Returns:\n
            list: A JSON object containing the requested information about the countries.\n
        Example: \n
            - To get single state with all the filters
                    ```
                    hawqal.getState(state_name="punjab")
                    ```\n
            - To get state of specific country
                    ```
                    hawqal.getState(country_name="Pakistan",state_name="punjab")
                    ```\n
            - To apply filters and exclude longitude
                    ```
                    hawqal.getStates(state_name="punjab",filter=hawqal.StateFilter(longitude=False))
                    ```\n
        """
        if state_name == "":
            raise ValueError("state_name must be set")
        cursor = databaseConnection()
        query = "SELECT " + str(filter) + " FROM states "

        if len(country_name) > 0 and len(state_name) > 0:
            query = query + f'where country_name= "{string.capwords(country_name)}" and state_name= "{string.capwords(state_name)}"'
        elif len(country_name) > 0:
            query = query + \
                    f'where country_name= "{string.capwords(country_name)}"'
        elif len(state_name) > 0:
            query = query + \
                    f'where state_name= "{string.capwords(state_name)}"'
        query = query + " ORDER BY country_name"
        cursor.execute(query)
        return convertJson(cursor)
