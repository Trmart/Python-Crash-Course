# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as 
# keys in your dictionary. Create a dictionary of information about each city and 
# include the country that the city is in, its approximate population, and one fact 
# about that city. The keys for each city’s dictionary should be something like 
# country, population, and fact. Print the name of each city and all of the information you have stored about it.

cities = {'Tokyo' : {'country' : 'japan' , 'pop' : '13.96 million' , 'fact' : 'Tokyo, Japan is the most populated urban area in the world!'},
          'Coeur d Alene' : {'country' : 'United States' , 'pop' : '54,822' , 'fact' : 'I live here! We have the worlds longest floating docks!'} , 
            'Berlin' : {'country' : 'Germany' , 'pop' : '3.66 million' , 'fact' : 'This is the previous location of the Berlin Wall'}} 

for key, dicts in cities.items():
    print("Here are some cool facts about " + key.title() + ": ")
    for key,val in dicts.items():
        print(key.title() + ": " + val.title())
    print('\n')
