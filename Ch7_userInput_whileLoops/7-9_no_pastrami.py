# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure 
# the sandwich 'pastrami' appears in the list at least three times. Add code 
# near the beginning of your program to print a message saying the deli has 
# run out of pastrami, and then use a while loop to remove all occurrences of 
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up 
# in finished_sandwiches.

def no_pastrami():
    print("sorry for the inconvenience but the deli has ran out of pastrami for the day".title())
    sandwhich_orders = ['blt', 'pastrami','ruben' ,'pastrami', 'italian','pastrami']

    while('pastrami' in sandwhich_orders):
        sandwhich_orders.remove('pastrami')
        
    for sandwich in sandwhich_orders:
        print("Your " + str(sandwich).title() + " is ready to go!".title())

def main():
    no_pastrami()

if(__name__ == '__main__'):
    main()