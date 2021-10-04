# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five 
# simple foods, and store them in a tuple.
# •	 Use a for loop to print each food the restaurant offers.
# •	 Try to modify one of the items, and make sure that Python rejects the 
# change.
# •	 The restaurant changes its menu, replacing two of the items with different 
# foods. Add a block of code that rewrites the tuple, and then use a for
# loop to print each of the items on the revised menu.

buffet_menu = ('Pizza', 'Fried Chicken' , 'Steak' , 'Pasta' , 'Ribs') #using parenthisis instead of brackets defines a touple, kind of like a const arr in C++

for choice in buffet_menu:
    print("One of the items on the buffet menu tonight is: " + choice)

buffet_menu = ('Brisket','Wings','Calzone','Soup') # you cannot change the values in the touple, but you can overwrite the variable that stores the touple ;) 

for choice in buffet_menu:
    print("One of the items on the buffet menu tonight is: " + choice)
