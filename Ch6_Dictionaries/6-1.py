# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You 
# should have keys such as first_name, last_name, age, and city. Print each 
# piece of information stored in your dictionary.

person = {'first_name': 'Taylor', 'last_name': 'Martin' , 'age' : '27' , 'city' : 'Coeur d Alene'}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

person['major'] = 'Computer Science'

print(person['major'])

del person['major']

person['age'] = 26 

print(person['age'])
