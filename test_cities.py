import unittest
from city_functions import city_country

class TestCity(unittest.TestCase):
    """testear la funcion city_country"""

    def test_city_country(self):
        formatted_country = city_country('Santiago', 'Chile', '20.000.000')
        self.assertEqual(formatted_country,'Santiago Chile 20.000.000')

unittest.main()