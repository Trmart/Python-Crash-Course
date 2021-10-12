# 6-8. Pets: Make several dictionaries, where the name of each dictionary is the 
# name of a pet. In each dictionary, include the kind of animal and the owner’s 
# name. Store these dictionaries in a list called pets. Next, loop through your list 
# and as you do print everything you know about each pet

brutus= {'name' : 'brutus','animal' : 'dog' , 'owner' : 'Taylor'}
hammond= {'name' : 'hammond','animal' : 'hamster' , 'owner' : 'Dave'}
winston= {'name' : 'winston','animal' : 'gorilla' , 'owner' : 'joe'}
casey= {'name' : 'casey','animal' : 'cat' , 'owner' : 'lauren'}
rango= {'name' : 'rango','animal' : 'cameleon' , 'owner' : 'clint'}

pets_list = [brutus,hammond,winston,casey,rango]

for pet in pets_list:
    for key,val in pet.items():
        print(key.title() + ": " + val.title())
    print()