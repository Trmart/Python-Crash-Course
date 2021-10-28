# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write 
# a class called IceCreamStand that inherits from the Restaurant class you wrote 
# in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of 
# the class will work; just pick the one you like better. Add an attribute called 
# flavors that stores a list of ice cream flavors. Write a method that displays 
# these flavors. Create an instance of IceCreamStand, and call this method.

class Restaurant():
    """A Simple class example in Python to model restaurant info"""
    # __init__() is similar to a class constructor in C++ 
    def __init__(self,restaurant_name, cuisine_type):  
        """Initialize name and cuisine attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints the two pieces of info about the restaurant sent into it"""
        print(str(self.restaurant_name).title() + ' Specializes In '  + str(self.cuisine_type).title() + ' Cuisine')

    def open_restaurant(self):
        """prints a message indicating the restaurant is open"""
        print(str(self.restaurant_name).title() + " is open and ready for business!".title())

class IceCreamStand(Restaurant):
    """A specific restuarant subclass IceCreamStand that inherits from the superclass Restuarant"""
    def __init__(self,restaurant_name,cuisine_type) -> None:
        """Uses super() to inherit __init__() methods from the parent(super) class"""
        super().__init__(restaurant_name,cuisine_type)
    
    flavors = ['vanilla','chocolate','strawberry','poop']

    def print_flavors_list(self):
        """this function prints a list of flavors"""
        for flavor in self.flavors:
            print(str(flavor).title())
def main():
    """main function"""
    cold_stone = IceCreamStand('cold stone','ice cream')
    cold_stone.open_restaurant()
    cold_stone.describe_restaurant()
    print(str(cold_stone.restaurant_name).title() + ' flavors list:'.title())
    cold_stone.print_flavors_list()

if(__name__=='__main__'):
    main()