from dal.dao import databaseConnection
import string
import os
import json
from .filters.city_filter import CityFilter
from Json.Query import convertJson


class City:

    @staticmethod
    def getCities(country_name="", state_name="", filter=CityFilter()):
        """
        It takes 3 optional parameters and return JSON object.\n
        Default: \n
                By default it will return all the cities with all the fields including
                - city_id\n
        Args:\n
                    country_name (str): Optional - To get the cities of some specific country.\n
                    state_name (str): Optional - To get the cities of some specific state.\n
                    filters (CityFilter): Optional - A class object specifying which fields to include in the results.\n
        Returns:\n
                    list: A json object containing the requested information about the cities.\n
        Example: \n
            - To get all cities
                    ```
                    hawqal.getCities()
                    ```\n
            - To get all cities of some country
                    ```
                    hawqal.getCities(country_name="Pakistan")
                    ```\n
            -  To get all cities of some state in a country
                    ```
                    hawqal.getCities(country_name="Pakistan",state_name="Punjab")
                    ```\n
            - To apply filters and exclude state_name
                    ```
                    hawqal.getCities(filter=hawqal.CityFilter(state_name=False))
                    ```
        """
        cursor = databaseConnection()
        query = "SELECT " + str(filter) + " FROM cities"

        if country_name != "":
            query = query + \
                f" WHERE country_name = '{string.capwords(country_name)}'"
        elif state_name != "":
            query = query + \
                f" WHERE state_name = '{string.capwords(state_name)}'"

        cursor.execute(query)

        return convertJson(cursor)

    @ staticmethod
    def getCity(country_name="", state_name="", city_name="", filters=CityFilter()):
        """
        Retrieves information about a city from the database.\n
        Parameters:\n
                    country_name (str): The name of the country where the city is located. Optional.\n
                    state_name (str): The name of the state or province where the city is located. Optional.\n
                    city_name (str): The name of the city. Required.\n
                    filters (CityFilter): An object specifying which fields to include in the results. Optional.\n
        Returns:\n
                    A Json object containing the requested information about the city.\n
        Raises:\n
                    ValueError: If `city_name` is not specified.
        """
        cursor = databaseConnection()
        if city_name == "":
            raise ValueError("City name must be set")
        query = "SELECT " + str(filters) + " FROM CITIES "
        if country_name != "":
            query = query +\
                f"WHERE country_name='{string.capwords(country_name)}' AND city_name='{string.capwords(city_name)}' "
        elif state_name != "":
            query = query +\
                f"Where state_name='{string.capwords(state_name)}' and city_name='{string.capwords(city_name)}'"
        elif country_name != "" and state_name != "":
            query = query +\
                f"Where state_name='{string.capwords(state_name)}' and country_name='{string.capwords(country_name)} and city_name='{string.capwords(city_name)}' '"
        else:
            query = query + f"where city_name='{string.capwords(city_name)}'"

        cursor.execute(query)

        return convertJson(cursor)
