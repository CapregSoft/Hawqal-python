import unittest
from hawqal.country import Country
from hawqal.states import States
from hawqal.cities import City
from hawqal.currency import Currency


class TestFunc(unittest.TestCase):

    def test_getCountries(self):
        self.assertEqual(len(Country.getCountries()), 250)

    def test_getStates(self):
        self.assertEqual(len(States.getStates()), 4989)
        self.assertEqual(len(States.getStates("pakistan")), 8)

    def test_getCities(self):
        self.assertEqual(len(City.getCities()), 150710)
        self.assertEqual(len(City.getCities("pakistan")), 458)
        self.assertEqual(len(City.getCities("", "sindh")), 119)

    def test_getCurrency(self):
        self.assertEqual(len(Currency.getCurrency()), 250)
        self.assertEqual(len(Currency.getCurrency("Pakistan")), 3)


if __name__ == '__main__':
    unittest.main()
