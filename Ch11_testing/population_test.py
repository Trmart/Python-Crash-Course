import unittest
from population import city_country

class TestPopulation(unittest.TestCase):
    """class to test a function"""
    def test_pop(self):
        """tests city_country with optional pop perameter"""
        formatted_name =  city_country('couer d alene','united states','53,524')
        self.assertEqual(formatted_name,'Couer D Alene,United States Population:53,524')
    
    def test_city_country(self):
        """tests city_country without pop perameter"""
        formatted_name =  city_country('couer d alene','united states')
        self.assertEqual(formatted_name,'Couer D Alene,United States')
unittest.main()