from dal.dao import Database
from filter.filter import Filter
import string
import os


class City:
    """
        1. Countries function takes two parameters as input country name and filters.\n
        2. By default, function will return countries name.\n
        3. Additional fields are included in filter.\n
        4. From filter of boolean TRUE fields will be included in output
            e.g
                {
                    "coordinates": True,
                    "country": True,
                    "state":True
                }
        """

    @staticmethod
    def getCities(country="", state="", meta={}):
        if isinstance(country, str):
            country = string.capwords(country)
        if isinstance(state, str):
            state = string.capwords(state)
        dirname = os.path.dirname(__file__)
        file_name = os.path.join(
            dirname, '..', 'database', 'hawqalDB.sqlite')
        with open(file_name, 'r', encoding="utf8") as db:
            database = Database(file_name).makeConnection()
            cursor = database.cursor()
        if state == "" and country == "" and len(meta) == 0:
            data = cursor.execute(
                f"SELECT city_name FROM cities ORDER BY city_name")
            cities = [city[0] for city in data]
            return cities
        elif country != "" and type(country) != type({}) and state == "" and len(meta) == 0:

            data = cursor.execute(
                f"SELECT city_name FROM cities WHERE country_name = '{country}'")
            cities = [city[0] for city in data]
            return cities
        elif country != "" and type(country) != type({}) and state == "" and len(meta) > 0:
            selectedFields = Filter.CityFilters(meta)
            data = cursor.execute(
                f"SELECT city_name,{selectedFields} FROM cities WHERE country_name = '{country}'")
            cities = [list(city) for city in data]
            return cities
        elif country == "" and state != "" and len(meta) == 0:
            data = cursor.execute(
                f"SELECT cities.city_name FROM cities,states WHERE cities.state_id == states.state_id AND "
                f"states.state_name == '{state}'")
            return [city[0] for city in data]
        elif country != "" and state != "" and type(state) != type({}) and len(meta) > 0:
            selectedFields = Filter.CityFilters(meta)
            data = cursor.execute(
                f"SELECT city_name,{selectedFields} FROM cities WHERE country_name = '{country}'")
            cities = [list(city) for city in data]
            return cities
        elif country != "" and state != "" and type(state) != type({}) and len(meta) == 0:
            data = cursor.execute(f"SELECT cities.city_name,states.state_name,countries.country_name FROM cities,"
                                  f"states,countries WHERE cities.state_id == states.state_id AND states.state_name "
                                  f"== '{state}' AND  cities.country_name== countries.country_name AND "
                                  f"countries.country_name == '{country}';")
            cities = [list(city) for city in data]
            return cities
        elif country == "" and state != "" and len(meta) > 0:
            selectedFields = Filter.CityFilters(meta)
            data = cursor.execute(
                f"SELECT cities.city_name,{selectedFields} FROM cities,states WHERE cities.state_id == "
                f"states.state_id AND states.state_name == '{state}'")
            return [list(city) for city in list(data)]
        elif country == "" and state == "" and len(meta) > 0:
            selectedFields = Filter.CityFilters(meta)
            data = cursor.execute(
                f"SELECT cities.city_name,{selectedFields}  FROM cities ORDER BY city_name")
            return [list(city) for city in list(data)]
        # elif any(isinstance(arg, dict) for arg in (country, state, meta)):
        #     if (country == type({})):
        #         meta, country, state = country, "", ""
        #     else:
        #         meta, country, state = state, "", ""
        #     selectedFields = Filter.CityFilters(meta)
        #     data = cursor.execute(f"SELECT cities.city_name,{selectedFields}  FROM cities ORDER BY city_name")
        #     return [list(city) for city in list(data)]
