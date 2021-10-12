# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop 
# through the list of sandwich orders and print a message for each order, such 
# as I made your tuna sandwich. As each sandwich is made, move it to the list 
# of finished sandwiches. After all the sandwiches have been made, print a 
# message listing each sandwich that was made.

def deli_ordering():
    sandwhich_orders = ['blt', 'ruben' , 'italian']
    finished_sandwiches = []

    while(sandwhich_orders):
        current_order = sandwhich_orders.pop()
        print("i am currently preparing your ".title() + current_order.title())
        finished_sandwiches.append(current_order)
    
    for sandwhich in finished_sandwiches:
        print("Your " + str(sandwhich).title() + " is finished and ready to go!".title())
    
    print("Thank you for dining with us today! i hope to see you soon".title())


def main():
    deli_ordering()

if(__name__ == '__main__'):
    main() 


