# 9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
# Add an attribute called number_served with a default value of 0. Create an 
# instance called restaurant from this class. Print the number of customers the 
# restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number 
# of customers that have been served. Call this method with a new number and 
# print the value again.
# Add a method called increment_number_served() that lets you increment 
# the number of customers who’ve been served. Call this method with any number you 
# like that could represent how many customers were served in, say, a 
# day of business.
class Restaurant():
    """A Simple class example in Python to model restaurant info"""
    # __init__() is similar to a class constructor in C++ 
    def __init__(self,restaurant_name, cuisine_type):  
        """Initialize name and cuisine attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints the two pieces of info about the restaurant sent into it"""
        print(self.restaurant_name + ' Specializes In '  + self.cuisine_type + 'Cuisine')

    def open_restaurant(self):
        """prints a message indicating the restaurant is open"""
        print(self.restaurant_name + " is open and ready for business!".title())

    def set_num_served(self,number_of_customers):
        """Setter function to set number of customers served"""
        self.number_served = number_of_customers
    
    def increment_number_served(self,number_of_customers):
        """increments number_served by the number sent in"""
        self.number_served += number_of_customers

def main():
    """main function"""
    crown_and_thistle = Restaurant('Crown & Thistle','British Pub ')

    print(crown_and_thistle.restaurant_name)
    print(crown_and_thistle.cuisine_type)
    
    crown_and_thistle.open_restaurant()
    crown_and_thistle.describe_restaurant()
    print(crown_and_thistle.number_served)
    
    crown_and_thistle.number_served = 10
    print(crown_and_thistle.number_served)

    crown_and_thistle.set_num_served(100)
    print(crown_and_thistle.number_served)

    crown_and_thistle.increment_number_served(2500)
    print(crown_and_thistle.number_served)

if(__name__=='__main__'):
    main()