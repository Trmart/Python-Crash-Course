# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on 
# a person’s age. If a person is under the age of 3, the ticket is free; if they are 
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is 
# $15. Write a loop in which you ask users their age, and then tell them the cost 
# of their movie ticket.

def ticket_cost():
    print("this program allows you to enter your age and compute how much your movie ticket will cost\n".title())
    active = True
    while(active):
        user_age = input("please enter your age to get your movie ticket price:(enter -1 to quit): ".title())
        user_age = int(user_age)

        if(user_age > 0 and user_age < 3):
            print("tickets for children under the age of 3 are free! \n".title())
        if(user_age > 3 and user_age <= 12):
            print("tickets for children between age 3-12 are $10\n".title())
        if(user_age > 12):
            print("for people older than age 12 tickets are $15\n ".title())
        if(user_age == -1):
            print("exiting program, goodbye".title())
            active = False


#syntax below is how to define a main function/method in Python. Like int main() in C++
def main():
    ticket_cost()

if(__name__ == "__main__"):
    main()