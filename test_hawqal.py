import unittest
from hawqal.country import Country
from hawqal.states import StatesByCountry
from hawqal.cities import City
from hawqal.citiesbycountry import CitiesByCountry


class TestFunc(unittest.TestCase):

    def test_getCountries(self):
        self.assertEqual(len(Country.getCountries()), 250)

    def test_getStates(self):
        self.assertEqual(len(StatesByCountry.getStates("Pakistan")), 8)

    def test_getCities(self):
        self.assertEqual(len(City.getCities("Pakistan", "Punjab")), 214)

    def test_getCitiesByCountry(self):
        expected = len(CitiesByCountry.getCities("Pakistan"))
        self.assertEqual(
            len(CitiesByCountry.getCities("Pakistan")), expected)


if __name__ == '__main__':
    unittest.main()
