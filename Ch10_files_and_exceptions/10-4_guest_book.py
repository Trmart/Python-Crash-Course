# 10-4. Guest Book: Write a while loop that prompts users for their name. When 
# they enter their name, print a greeting to the screen and add a line recording 
# their visit in a file called guest_book.txt. Make sure each entry appears on a 
# new line in the file.

def main():
    """main"""

    file_name = 'guest_book.txt'
    while(True):
        print('please enter your name and i will write it to a file and print a greeting'.title())
        name = input('please enter your name(or enter quit to exit):')
        
        if(name.lower() == 'quit'):
            exit(1)
        
        print("Hello " + name.title() + ' thank you for staying with us!'.title())
        
        with open(file_name,'w') as file_object:
            file_object.write('thank you for staying with us '.title() + name.title())




if(__name__=='__main__'):
    main()

