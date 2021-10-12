# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three 
# names to use as keys in the dictionary, and store one to three favorite places 
# for each person. To make this exercise a bit more interesting, ask some friends 
# to name a few of their favorite places. Loop through the dictionary, and print 
# each person’s name and their favorite places.

favorite_places = {'joe' : ['Los Angles', 'Las Vegas'] , 'bob' : ['portland','spokane','new york'] , 'taylor' : ['CDA','kona' , 'spokane' , 'moscow']}

for name, places in favorite_places.items():
    print(name.title() + "'s favorite places are: ")
    for place in places:
        print(place.title())
    print('\n')
