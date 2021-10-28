# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three 
# different instances from the class, and call describe_restaurant() for each 
# instance.

class Restaurant():
    """A Simple class example in Python to model restaurant info"""
    # __init__() is similar to a class constructor in C++ 
    def __init__(self,restaurant_name, cuisine_type):
        """Initialize name and cuisine attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints the two pieces of info about the restaurant sent into it"""
        print(str(self.restaurant_name + ' Specializes In '  + self.cuisine_type).title() + ' Cuisine')
        print()

    def open_restaurant(self):
        """prints a message indicating the restaurant is open"""
        print(str(self.restaurant_name + " is open and ready for business!").title())
        
def main():
    """main function"""
    crown_and_thistle = Restaurant('Crown & Thistle','British Pub')
    syringa = Restaurant('syringa','japanese')
    cafe_carambola = Restaurant('cafe carambola', 'mexican')

    crown_and_thistle.open_restaurant()
    crown_and_thistle.describe_restaurant()

    syringa.open_restaurant()
    syringa.describe_restaurant()

    cafe_carambola.open_restaurant()
    cafe_carambola.describe_restaurant()

if(__name__=='__main__'):
    main()