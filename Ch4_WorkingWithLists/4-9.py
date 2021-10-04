# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the 
# first 10 cubes.

cubes = list(value**3 for value in range(1,11)) #list comprehension? made each element of list a list of the first ten cubes 

for cube in cubes:
    print(cubes)

cubes_ver2 = [value**3 for value in range(1,11)] #list comprehension, (definition for expression, for loop, range)

for cube in cubes_ver2:
    print(cube)