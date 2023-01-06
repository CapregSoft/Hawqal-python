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
        Description:\n
                getCities function returns data of cities w.r.t to country or state in JSON format
        Default: \n
                By default it will return all the cities with all the fields including\n
                - city_id\n
                - country_name\n
                - city_name\n
                - state_id\n
                - state_name\n
                - latitude\n
                - longitude\n
        Args:\n
                country_name (str): Optional : To get the cities of some specific country.\n
                state_name (str): Optional : To get the cities of some specific state.\n
                filters (CityFilter): Optional : A class object specifying which fields to include in the results.\n
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

        if country_name != "" and state_name != "":
            query = query + \
                f" WHERE country_name = '{string.capwords(country_name)}' AND state_name = '{string.capwords(state_name)}'"
        elif country_name != "":
            query = query + \
                f" WHERE country_name = '{string.capwords(country_name)}'"
        elif state_name != "":
            query = query + \
                f" WHERE state_name = '{string.capwords(state_name)}'"

        cursor.execute(query)

        return convertJson(cursor)

    @staticmethod
    def getCity(country_name="", state_name="", city_name="", filters=CityFilter()):
        """
        Description:\n
                getCity function returns data of a single city JSON format
        Default: \n
                By default it will return data of a city if we provide that in the function with all the field
                including\n
                - city_id\n
                - country_name\n
                - city_name\n
                - state_id\n
                - state_name\n
                - latitude\n
                - longitude\n
        Args:\n
                    country_name (str): Optional : To get the cities of some specific country.\n
                    state_name (str): Optional : To get the cities of some specific state.\n
                    city_name (str): Required : To get the city.\n
                    filters (CityFilter): Optional : A class object specifying which fields to include in the results.\n
        Returns:\n
                    list: A JSON object containing the requested information about the cities.\n
        Example: \n
            - To get single city with all the filters
                    ```
                    hawqal.getCity(city_name="wah")
                    ```\n
            - To get city of specific country
                    ```
                    hawqal.getCity(country_name="Pakistan",city_name="wah")
                    ```\n
            -  To get city of specific state
                    ```
                    hawqal.getCity(state_name="punjab",city_name="wah")
                    ```\n
            -  To get city of specific state and country
                    ```
                    hawqal.getCity(country_name="pakistan",state_name="punjab",city_name="wah")
                    ```\n
            - To apply filters and exclude longitude
                    ```
                    hawqal.getCity(country_name="pakistan",state_name="punjab",city_name="wah",filter=hawqal.CityFilter(longitude=False))
                    ```
        """
        cursor = databaseConnection()
        if city_name == "":
            raise ValueError("City name must be set")
        query = "SELECT " + str(filters) + " FROM CITIES "
        if country_name != "":
            query = query + \
                f"WHERE country_name='{string.capwords(country_name)}' AND city_name='{string.capwords(city_name)}' "
        elif state_name != "":
            query = query + \
                f"Where state_name='{string.capwords(state_name)}' and city_name='{string.capwords(city_name)}'"
        elif country_name != "" and state_name != "":
            query = query + \
                f"Where state_name='{string.capwords(state_name)}' and country_name='{string.capwords(country_name)} and city_name='{string.capwords(city_name)}' '"
        else:
            query = query + f"where city_name='{string.capwords(city_name)}'"

        cursor.execute(query)

        return convertJson(cursor)
