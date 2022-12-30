from dal.dao import Database
from filter.filter import Filter
import string
import os


class States:

    '''
    1. States function takes two parameters as input state name and filters.\n
    2. By default function will return states name.\n
    3. Addtional fields are included in filter.\n
    4. From filter of boolean TRUE fields will be included in output
        e.g
            {
                "coordinates":True
            }

    '''

    @staticmethod
    def getStates(country="", meta={}):
        dirname = os.path.dirname(__file__)
        file_name = os.path.join(
            dirname, '..', 'database', 'hawqalDB.sqlite')
        with open(file_name, 'r', encoding="utf8") as db:
            database = Database(file_name).makeConnection()
            cursor = database.cursor()
        if country == "" and len(meta) == 0:
            data = cursor.execute(
                f'SELECT state_name FROM states')
            return [state[0] for state in data]
        elif type(country) == type({}):
            if type(meta) == type(""):
                if meta != "":
                    selectedFields = Filter.CountryFilter(country)
                    meta = string.capwords(meta)
                    data = cursor.execute(
                        f'SELECT state_name,{selectedFields} FROM states WHERE country_name = "{meta}"')
                    return [list(country) for country in data]
                else:
                    meta, country = country, ""
                    selectedFields = Filter.StateFilter(meta)
                    data = cursor.execute(
                        f'SELECT state_name,{selectedFields} FROM states')
                    return [list(country) for country in data]
        elif country != "" and len(meta) > 0:
            country = string.capwords(country)
            selectedFields = Filter.StateFilter(meta)
            data = cursor.execute(
                f'SELECT state_name,{selectedFields} FROM states WHERE country_name = "{country}"')
            return [list(country) for country in data]
        elif country != "" and len(meta) == 0:
            country = string.capwords(country)
            selectedFields = Filter.StateFilter(meta)
            data = cursor.execute(
                f'SELECT state_name FROM states WHERE country_name = "{country}"')
            return [country[0] for country in list(data)]
