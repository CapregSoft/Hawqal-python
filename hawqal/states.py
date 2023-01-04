from dal.dao import Database
from filter.filter import Filter
import string
import os


class States:

    @staticmethod
    def getStates(country_name="", meta={}):
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

        query = "SELECT"

        if len(meta)>0:
            selectedFields = Filter.StateFilter(meta)
            query = query + f' {selectedFields}'
        elif len(meta)==0:
            query = query + " *"

        query = query + " FROM states"

        if len(country_name)>0:
            query=query+ f' where country_name= "{string.capwords(country_name)}"'

        cursor.execute(query)

        data_json = []
        header = [i[0] for i in curr.description]
        data = cursor.fetchall()
        for i in data:
            data_json.append(dict(zip(header, i)))
        return data_json


    @staticmethod
    def getState(country_name="",state_name="", meta={}):
        
        file_name = os.path.join(
            os.path.dirname(__file__), '..', 'database', 'hawqalDB.sqlite')

        with open(file_name, 'r', encoding="utf8") as db:
            database = Database(file_name).makeConnection()
            cursor = database.cursor()

        query = "SELECT"

        if len(meta)>0:
            selectedFields = Filter.StateFilter(meta)
            query = query + f' {selectedFields}'
        elif len(meta)==0:
            query = query + " *"

        query = query + " FROM states where"

        if len(country_name)>0 and len(state_name)>0:
            query = f' country_name= "{string.capwords(country_name)}" and state_name= "{string.capwords(state_name)}"'
        elif len(country_name)>0:
            query=query+ f' country_name= "{string.capwords(country_name)}"'
        elif len(state_name)>0:       
            query=query+ f' state_name= "{string.capwords(state_name)}"'

        query = query + " ORDER BY country_name"

        data_json = []
        header = [i[0] for i in curr.description]
        data = cursor.fetchall()
        for i in data:
            data_json.append(dict(zip(header, i)))
        return data_json