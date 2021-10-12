# 7-2. Restaurant Seating: Write a program that asks the user how many people 
# are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. 
# Otherwise, report that their table is ready

num_patrons = input("Please Enter the Number of People that Will Dine With Your Group Tonight: ")

num_patrons = int(num_patrons)

if(num_patrons > 8):
    print("My apologies, your party will have to wait for a table")
if(num_patrons > 0 and num_patrons <= 8):
    print("Perfect, looks like we have a table ready for your party!")