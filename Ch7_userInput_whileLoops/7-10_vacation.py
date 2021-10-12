# 7-10. Dream Vacation: Write a program that polls users about their dream 
# vacation. Write a prompt similar to If you could visit one place in the world, 
# where would you go? Include a block of code that prints the results of the poll.

def dream_vacation():
    print("this program takes a poll from the user asking where they would want to vacation ".title())

    active = True
    vacations_list = {}
    
    while(active):
        current_name = input("\nplease input your name: ".title())
        current_location = input("\nplease enter where you would like to vacation: ".title())
        
        vacations_list[current_name] = current_location

        repeat = input("\nwould you like to take the poll again? yes or no: ".title())

        if(repeat.lower()=='no'):
            active = False
        
    for name,vacation in vacations_list.items():
        print('\n' + str(name + "'s").title() + " dream vacation is " + str(vacation).title()) 

def main():
    dream_vacation()

if(__name__ == '__main__'):
    main()