# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so 
# each person can have more than one favorite number. Then print each person’s 
# name along with their favorite numbers.

fav_nums = {'joe' : [5,6] , 'bob' : [12,14,16] , 'dave' : [72,48,36,99]}

for name, nums in fav_nums.items():
    print(name.title() + "'s " + "favorite numbers are: ")
    for num in nums:
        print(num)
    print('\n')
