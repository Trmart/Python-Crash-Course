# 6-6. Polling: Use the code in favorite_languages.py (page 104).
# •	 Make a list of people who should take the favorite languages poll. Include 
# some names that are already in the dictionary and some that are not.
# •	 Loop through the list of people who should take the poll. If they have 
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take 
# the poll.

pollArr = ['Jordan' , 'Joe' , 'Taylor']

favLanguages = {'David':'Java' , 'Jeff': 'C#', 'Taylor':'Python'}

for people in pollArr:
    if(people in favLanguages):
        print(people + " Thank you for taking the poll!")
    else:
        print(people + " I invite you to please take the favorite programming language poll!")
