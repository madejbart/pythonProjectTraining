import unittest
from city_functions import get_formatted_city_country

class CountryCityTest(unittest.TestCase):
    """ Tests forcity_functions.py  """

    def test_city_country(self):
        formatedcityandcountry = get_formatted_city_country('santiago', 'chile')
        self.assertEqual(formatedcityandcountry, 'Santiago, Chile - Population:')

    def test_city_country_population(self):
        formatedstring = get_formatted_city_country('santiago', 'chile', 5000000)
        self.assertEqual(formatedstring, 'Santiago, Chile - Population:5000000')

if __name__ == '__main__':
    unittest.main()



