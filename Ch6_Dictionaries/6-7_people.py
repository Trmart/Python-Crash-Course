# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
# Make two new dictionaries representing different people, and store all three 
# dictionaries in a list called people. Loop through your list of people. As you 
# loop through the list, print everything you know about each person.

user_1 = {'first_name': 'Taylor', 'last_name': 'Martin' , 'age' : '27' , 'city' : 'Coeur d Alene'}
user_2 = {'first_name': 'Joe', 'last_name': 'Smith' , 'age' : '28' , 'city' : 'Spokane'}
user_3 = {'first_name': 'Dave', 'last_name': 'Wilkenson' , 'age' : '43' , 'city' : 'Kona'}

people_list = [user_1,user_2,user_3]

for people in people_list:
    print(people)
