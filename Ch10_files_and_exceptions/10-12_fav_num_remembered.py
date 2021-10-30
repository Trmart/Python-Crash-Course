# 10-12. Favorite Number Remembered: Combine the two programs from 
# Exercise 10-11 into one file. If the number is already stored, report the favorite 
# number to the user. If not, prompt for the user’s favorite number and store it in a 
# file. Run the program twice to see that it works.

import json
def write_fav_num():
    """writes user input data to a json file"""

    file_name = 'fav_num.json'
    fav_num = input('please enter your favorite number: '.title())
    with open(file_name,'w') as file_object:
        json.dump(fav_num,file_object)
        print('we have stored and memorized your favorite number!')

            
def read_fav_num():
    """this function reads data from a json file"""

    file_name = 'fav_num.json'
    
    try:
        with open(file_name) as file_object:
            fav_num = json.load(file_object)
    
    except FileNotFoundError:
        print('the file' + file_name + ' was not found')
        fav_num = input('please enter your favorite number: '.title())
        with open(file_name,'w') as file_object:
            json.dump(fav_num,file_object)
            print('we have stored and memorized your favorite number!')
    else:
        print("I know your favorite number! It's " + fav_num)

def main():
    """main"""
    
    write_fav_num()
    read_fav_num()

if(__name__ == '__main__'):
    main()