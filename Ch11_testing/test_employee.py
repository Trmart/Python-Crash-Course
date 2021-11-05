import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """test class to test Employee class and member functions in employee module"""

    def setUp(self):
        """defines test cases for multiple uses"""
        self.employee = Employee('john','doe',100000)
        self.default_raise = self.employee.give_raise()
        self.custom_raise = self.employee.give_raise(20000)
    
    def test_give_default_raise(self):
        """tests give_raise with default raise"""
        employee = self.employee
        self.assertEqual(employee.give_raise(),self.default_raise)
    
    def test_give_custom_raise(self):
        """tests give_raise with custom raise amount"""
        employee = self.employee
        self.assertEqual(employee.give_raise(20000),self.custom_raise)

unittest.main()