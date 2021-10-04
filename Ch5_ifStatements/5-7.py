# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of 
# independent if statements that check for certain fruits in your list.
# •	 Make a list of your three favorite fruits and call it favorite_fruits.
# •	 Write five if statements. Each should check whether a certain kind of fruit 
# is in your list. If the fruit is in your list, the if block should print a statement, 
# such as You really like bananas!

fav_fruit = ['Peach','Strawberry','Watermelon']

for fruit in fav_fruit:
    if(fruit.lower() == "pear"):
        print("wow you really like " + fruit)
    elif(fruit.lower() == "apple"):
        print("wow you really like " + fruit)
    elif(fruit.lower() == "blueberry"):
        print("wow you really like " + fruit)
    elif(fruit.lower() == "peach"):
        print("wow you really like " + fruit)
    