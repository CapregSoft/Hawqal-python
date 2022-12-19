import unittest
from hawqal.services.country import Country
from hawqal.services.states import State
from hawqal.services.cities import City
from hawqal.services.statesbycountry import StatesByCountry
from hawqal.services.citiesbycountry import CitiesByCountry


class TestFunc(unittest.TestCase):

    def test_getCountries(self):
        self.assertEqual(len(Country.getCountries()), 250)

    def test_getStates(self):
        self.assertEqual(len(State.getStates()), 4989)

    def test_getCities(self):
        self.assertEqual(len(City.getCities()), 150710)

    def test_getStatesByCountry(self):
        expected = len(StatesByCountry.getStates("Pakistan"))
        self.assertEqual(len(StatesByCountry.getStates("Pakistan")), expected)

    def test_getCitiesByCountry(self):
        expected = len(CitiesByCountry.getCities("Pakistan"))
        self.assertEqual(len(CitiesByCountry.getCities("Pakistan")), expected)


if __name__ == '__main__':
    unittest.main()
