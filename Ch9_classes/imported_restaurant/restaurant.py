
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