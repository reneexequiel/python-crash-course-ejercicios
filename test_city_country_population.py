import unittest
from city_functions import city_country

class TestPopulation(unittest.TestCase):
    """testear la funcion city_country_population"""

    def test_city_country_population(self):
        formatted_populaton = city_country('Santiago', 'Chile', '20.000.000')
        self.assertEqual(formatted_populaton,'Santiago Chile 20.000.000')

unittest.main()