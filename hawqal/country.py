from dal.dao import databaseConnection
from Json.Query import convertJson
from .filters.country_filter import CountryFilter
import string
import os


class Country:

    @staticmethod
    def getCountries(filter=CountryFilter()):
        """
        Description:\n
                Get information about multiple countries from the database
        Default: \n
                By default, this method returns data about all countries, including the following fields:\n
                - country_name\n
                - iso_code\n
                - phone_code\n
                - capital\n
                - currency\n
                - currency_name\n
                - currency_symbol\n
                - country_domain\n
                - region\n
                - subregion\n
                - timezone\n
                - zone_city\n
                - UTC\n
                - latitude\n
                - longitude\n
        Args:\n
                filters (CountryFilter): Optional : A class object specifying which fields to include in the results.\n
        Returns:\n
                list: A JSON object containing the requested information about the countries.\n
        Example: \n
            - To get all the countries
                ```
                hawqal.getCountries()
                ```
            - To apply filters and exclude longitude
                ```
            hawqal.getCountries(filter=hawqal.CountryFilter(longitude=False))
            ```
        """
        cursor = databaseConnection()
        query = "SELECT " + str(filter)

        query = query + " FROM countries ORDER BY country_name ASC"
        cursor.execute(query)

        return convertJson(cursor)

    @staticmethod
    def getCountry(country_name="", filter=CountryFilter()):
        """
        Description:\n
                Get information about a specific country from the database.
        Default:
                By default, this method returns data about a country, including the following fields:\n
                - country_name\n
                - iso_code\n
                - phone_code\n
                - capital\n
                - currency\n
                - currency_name\n
                - currency_symbol\n
                - country_domain\n
                - region\n
                - subregion\n
                - timezone\n
                - zone_city\n
                - UTC\n
                - latitude\n
                - longitude\n
        Args:\n
                    country_name (str): Required : Name of country
                    filters (CityFilter): Optional : A class object specifying which fields to include in the results.\n
        Returns:\n
                    list: A JSON object containing the requested information about the country.\n
        Example: \n
            - To get the specific country data
                    ```
                      hawqal.getCountry(country_name="pakistan")
                    ```
            - To apply filters and exclude longitude
                    ```
                    hawqal.getCountry(country_name="pakistan",filter=hawqal.CountryFilter(longitude=False))
                    ```
        """
        cursor = databaseConnection()
        if country_name == "":
            raise ValueError("country_name must be set")

        query = "SELECT " + str(filter) + " FROM countries"

        if country_name != "":
            query = query + \
                f" WHERE country_name = '{string.capwords(country_name)}' ORDER BY country_name ASC"

        cursor.execute(query)

        return convertJson(cursor)
