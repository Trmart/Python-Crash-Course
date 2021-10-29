# 9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant. Make a Restaurant instance, 
# and call one of Restaurant’s methods to show that the import statement is working properly.
from restaurant import Restaurant

def main():
    """main"""
    restaurant = Restaurant('kaiju','japanese')
    restaurant.describe_restaurant()
    restaurant.open_restaurant()
if(__name__=='__main__'):
    main()