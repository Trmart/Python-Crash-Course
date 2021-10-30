# 10-5. Programming Poll: Write a while loop that asks people why they like 
# programming. Each time someone enters a reason, add their reason to a file 
# that stores all the responses.

def main():
    """main"""

    file_name = 'poll.txt'
    while(True):
        poll = input('why do you like programming? tell me why or enter quit to exit:'.title())
        
        if(poll.lower() == 'quit'):
            exit(1)
        
        print(poll.title())
        
        with open(file_name,'w') as file_object:
            file_object.write(poll.title())




if(__name__=='__main__'):
    main()