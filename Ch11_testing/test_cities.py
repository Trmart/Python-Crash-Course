import unittest #we must import unittest to test code
from city_country import city_country #import the module and function we want to test

class CityCountryTest(unittest.TestCase): #we must inherit unittest.Testcase to test a function, for a test case
    
    def test_city_country(self):
        formatted_name=city_country('couer d alene','united states')
        self.assertEqual(formatted_name,'Couer D Alene,United States') 

unittest.main() #call unittest.main() to run test