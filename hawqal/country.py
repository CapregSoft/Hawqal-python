from dal.dao import Database
from .filters.filter import Filter
import os

class Country:

    @staticmethod
    def getCountries(meta={}):
        """
            1. Countries function takes two parameters as input country name and meta.\n
            2. By default, function will return countries name.\n
            3. Additional fields are included in filter.\n
            4. From meta TRUE fields will be included in output
                e.g
                    {
                        "coordinates": True,
                        "region": True,
                        "currency": True,
                        "timezone": True,
                        "capital": True
                    }

        """

        file_name = os.path.join(os.path.dirname(
            __file__), '..', 'database', 'hawqalDB.sqlite')

        with open(file_name, 'r', encoding="utf8") as db:
            database = Database(file_name).makeConnection()
            cursor = database.cursor()

        query = "SELECT"


        if len(meta) > 0:
            selectedFields = Filter.CountryFilter(meta)
            query = query + f' {selectedFields}'
        elif len(meta)==0:
            query=query+" * "
        
        query = query + " FROM countries ORDER BY country_name ASC"

        data = cursor.execute(query)
        return [country[0] for country in list(data)]
