from dal.dao import Database
import string
import os


def filterFields(meta):
    fields = ''
    keyArrtibutes = {
        "coordinates": 'latitude,longitude',
        "country": "country_name"
    }
    for key, value in meta.items():
        if value:
            fields = fields + keyArrtibutes[key]+','
    return fields[:-1]


class States:

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
            meta, country = country, ""
            selectedFields = filterFields(meta)
            data = cursor.execute(
                f'SELECT state_name,{selectedFields} FROM states')
            return [list(country) for country in data]
        elif country != "" and len(meta) > 0:
            country = string.capwords(country)
            selectedFields = filterFields(meta)
            data = cursor.execute(
                f'SELECT state_name,{selectedFields} FROM states WHERE country_name = "{country}"')
            return [list(country) for country in data]
        elif country != "" and len(meta) == 0:
            country = string.capwords(country)
            selectedFields = filterFields(meta)
            data = cursor.execute(
                f'SELECT state_name FROM states WHERE country_name = "{country}"')
            return [country[0] for country in list(data)]
