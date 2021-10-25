# 8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
# Write a function called make_great() that modifies the list of magicians by adding the phrase the Great to each magician’s name. Call show_magicians() to 
# see that the list has actually been modified.

def make_great(magicians,great_magicians):
    
    while (magicians):
        magician = magicians.pop()
        great_magicians.append(magician+' The Great')
def show_magicians(magicians):
    for magician in magicians:
        print('Hello', str(magician).title() , 'i love your magic show'.title())

def main():
    magicians = ['david blaine', 'harry houdini' , 'chris angel']
    great_magicians = []
    make_great(magicians,great_magicians)
    show_magicians(great_magicians)
if(__name__=='__main__'):
    main()