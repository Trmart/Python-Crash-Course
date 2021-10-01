programming_languages = ['C++', 'C' , 'C#', 'Python'] #defines a list in python, similar to an array in C and C++
print(programming_languages)

print(programming_languages[0]) # you can access elements of a list in Python like elements of an array in C++
print(programming_languages[1])
print(programming_languages[2])
print(programming_languages[3])

print(programming_languages[-1]) #-1 element in python returns the last item in the list

programming_languages.append('Java') # append adds to the end of a list
print(programming_languages)

games = [] #dynamic allocation of a list in python

games.append("Fallout")
games.append("Borderlands")
games.append("Bioshock")
games.append("Bloodborne")

print(games)

games.insert(2,'HollowKnight')

print(games[2])

del(games[4]) # delete will remove an element at a specific location. 
print(games)

games.pop() #removes element at end of list, or you can specify an element to remove

print(games)

games.remove('Fallout') # you can remove from an location in a list and by value

print(games)

games.append('Ghost of Tsushima')

games.sort() # sorts a list
print(games)

games.sort(reverse = True) #sorts list in reverse order 
print(games)

print(sorted(programming_languages)) #sorted temporary sorts the list

len(programming_languages) #finds length of list 