import json
import unittest
from hawqal.country import Country
from hawqal.states import States
from hawqal.cities import City
from hawqal.filters.country_filter import CountryFilter
from hawqal.filters.city_filter import CityFilter
from hawqal.filters.state_filter import StateFilter

class TestFunc(unittest.TestCase):

    def test_getCountries(self):
        self.assertEqual(len(json.loads(Country.getCountries())), 250)
        self.assertEqual(len(json.loads(Country.getCountry(country_name="pakistan"))),1)

    def test_getStates(self):
        self.assertEqual(len(json.loads(States.getStates())), 4989)
        self.assertEqual(len(json.loads(States.getState(country_name="pakistan",state_name="Punjab"))), 1)

    def test_getCities(self):
        self.assertEqual(len(json.loads(City.getCities())), 150710)
        self.assertEqual(len(json.loads(City.getCity(country_name="pakistan",state_name='punjab',city_name='wah'))), 1)


if __name__ == '__main__':
    unittest.main()
