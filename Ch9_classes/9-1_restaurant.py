# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for 
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of 
# information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

class Restaurant():
    """A Simple class example in Python to model restaurant info"""
    # __init__() is similar to a class constructor in C++ 
    def __init__(self,restaurant_name, cuisine_type):  
        """Initialize name and cuisine attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints the two pieces of info about the restaurant sent into it"""
        print(self.restaurant_name + ' Specializes In '  + self.cuisine_type + 'Cuisine')

    def open_restaurant(self):
        """prints a message indicating the restaurant is open"""
        print(self.restaurant_name + " is open and ready for business!".title())

def main():
    """main function"""
    crown_and_thistle = Restaurant('Crown & Thistle','British Pub ')
    print(crown_and_thistle.restaurant_name)
    print(crown_and_thistle.cuisine_type)
    crown_and_thistle.open_restaurant()
    crown_and_thistle.describe_restaurant()

if(__name__=='__main__'):
    main()