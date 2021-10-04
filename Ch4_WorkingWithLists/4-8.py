# 4-8. Cubes: A number raised to the third power is called a cube. For example, 
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that 
# is, the cube of each integer

cubes = []

for value in range(1,11):
    value = value**3
    cubes.append(value)

for cube in cubes:
    print(cube)
