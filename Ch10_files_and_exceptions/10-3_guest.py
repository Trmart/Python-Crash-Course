# 10-3. Guest: Write a program that prompts the user for their name. When they 
# respond, write their name to a file called guest.txt.

def main():
    """main"""
    
    print("please enter your name and will write it to a file".title())
    name = input('please enter your name:')
    
    with open('name.txt','w') as file_object:
        file_object.write(name)
    print('your name is now written in name.txt' )

if(__name__=='__main__'):
    main()