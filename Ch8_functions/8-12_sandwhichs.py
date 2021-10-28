# 8-12. Sandwiches: Write a function that accepts a list of items a person wants 
# on a sandwich. The function should have one parameter that collects as many 
# items as the function call provides, and it should print a summary of the sandwich that is being ordered. Call the function three times, 
# using a different number of arguments each time.

def make_me_a_sammich(*sammich_fixins):
    print('we are getting ready to make you a sammich with the following fixings: '.title())
    for fixin in sammich_fixins:
        print(fixin)
    print()
    
def main():
    make_me_a_sammich('Turkey')
    make_me_a_sammich('Ham','Swiss')
    make_me_a_sammich('Rye','Pastrami','Sauerkraut') 

if(__name__ == '__main__'):
    main()