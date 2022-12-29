import unittest
from hawqal.country import Country
from hawqal.states import States
from hawqal.cities import City


class TestFunc(unittest.TestCase):

    def test_getCountries(self):
        self.assertEqual(len(Country.getCountries()), 250)
        self.assertEqual(len(Country.getCountries(
            "pakistan", {"coordinates": True})), 3)

    def test_getStates(self):
        self.assertEqual(len(States.getStates()), 4989)
        self.assertEqual(len(States.getStates("pakistan")), 8)

    def test_getCities(self):
        self.assertEqual(len(City.getCities()), 150710)
        self.assertEqual(len(City.getCities("pakistan")), 458)


if __name__ == '__main__':
    unittest.main()
