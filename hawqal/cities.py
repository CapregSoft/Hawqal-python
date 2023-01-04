from dal.dao import create_cursor
import string
import os
from .filters.city_filter import CityFilter
from Json.Query import convertJson


class City:

    @staticmethod
    def getCities(country_name="", state_name="", filters=CityFilter()):
        """
        it takes 3 optional parameters and return JSON object.
        
        Default:
            By default it will return all the cities with all the fields including 
            
                - city_id
        
        Args:
            country_name (str): Optional - To get the cities of some specific country.
            state_name (str): Optional - To get the cities of some specific state.
            filters (CityFilter): Optional - A class object specifying which fields to include in the results.
        
        Returns:
            list: A json object containing the requested information about the cities.
            
        Example: 
            - To get all cities
            
                ```
                hawqal.getCities()
                ```
            
            - To get all cities of some country
            
                ```
                hawqal.getCities(country_name="Pakistan")
                ```
                
            -  To get all cities of some state in a country
            
                ```
                hawqal.getCities(country_name="Pakistan",state_name="Punjab")
                ```
                
            - To apply filters and exclude state_name
                ```
                hawqal.getCities(filter=hawqal.CityFilter(state_name=False))
                ```
        """
        cursor = create_cursor()
        query = "SELECT " + str(filters) + " FROM cities"

        if country_name != "":
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
        Retrieves information about a city from the database.
    
        Parameters:
        country_name (str): The name of the country where the city is located. Optional.
        state_name (str): The name of the state or province where the city is located. Optional.
        city_name (str): The name of the city. Required.
        filters (CityFilter): An object specifying which fields to include in the results. Optional.
        
        Returns:
        A Json object containing the requested information about the city.
        
        Raises:
        ValueError: If `city_name` is not specified.
        """
        cursor = create_cursor()
        country_name = string.capwords(country_name)
        state_name = string.capwords(state_name)
        city_name = string.capwords(city_name)
        if city_name == "":
            raise ValueError("City name must be set")
        query = "SELECT " + str(filters) + " FROM CITIES "
        if country_name != "":
            query = query + f"WHERE country_name='{country_name}' AND city_name='{city_name}' "
        elif state_name != "":
            query = query + f"Where state_name='{state_name}' and city_name='{city_name}'"
        elif country_name != "" and state_name != "":
            query = query + f"Where state_name='{state_name}' and country_name='{country_name} and city_name='{city_name}' '"
        else:
            query = query + f"where city_name='{city_name}'"

        cursor.execute(query)

        return convertJson(cursor)
