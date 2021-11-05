# 11-3. Employee: Write a class called Employee. The __init__() method should 
# take in a first name, a last name, and an annual salary, and store each of these 
# as attributes. Write a method called give_raise() that adds $5000 to the 
# annual salary by default but also accepts a different raise amount.
# Write a test case for Employee. Write two test methods, test_give_
# default_raise() and test_give_custom_raise(). Use the setUp() method so 
# you don’t have to create a new employee instance in each test method. Run 
# your test case, and make sure both tests pass.

class Employee():
    def __init__(self,first_name,last_name,annual_salary):
        """Employee class constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    
    def give_raise(self,default_salary_raise = 5000):
        """that adds $5000 to the # annual salary by default 
            but also accepts a different raise amount."""
        if(default_salary_raise):
            new_annual_salary = self.annual_salary + default_salary_raise
            return new_annual_salary
        else:
            return self.annual_salary+default_salary_raise
    