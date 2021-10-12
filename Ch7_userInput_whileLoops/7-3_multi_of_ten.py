# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the 
# number is a multiple of 10 or not.

user_num = input("Please Enter A Number, And I Will Tell You If It Is A Multiple Of Ten: ")

user_num = int(user_num)

if(user_num %10 == 0):
    print(str(user_num) + " Is A Multiple Ten")
else:
    print(str(user_num) + " Is Not A Multiple Of Ten")
