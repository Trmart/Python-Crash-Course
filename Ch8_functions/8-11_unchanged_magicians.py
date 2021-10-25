# 8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the 
# function make_great() with a copy of the list of magicians’ names. Because the 
# original list will be unchanged, return the new list and store it in a separate list.
# Call show_magicians() with each list to show that you have one list of the original names and one list with the Great added to each magician’s name

def make_great(magicians,great_magicians):
    
    while (magicians):
        magician = magicians.pop()
        great_magicians.append(magician+' The Great')
def show_magicians(magicians):
    for magician in magicians:
        print('Hello', str(magician).title() , 'i love your magic show'.title())
    print()

def main():
    magicians = ['david blaine', 'harry houdini' , 'chris angel']
    great_magicians = []
    make_great(magicians[:],great_magicians)
    print('original list of magicians:'.title())
    show_magicians(magicians)
    print('modified list: '.title())
    show_magicians(great_magicians)
    print('unchanged original list:'.title())
    show_magicians(magicians)
if(__name__=='__main__'):
    main()