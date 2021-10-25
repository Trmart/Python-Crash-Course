# 8-9. Magicians: Make a list of magician’s names. Pass the list to a function 
# called show_magicians(), which prints the name of each magician in the list.

def show_magicians(magicians):
    for magician in magicians:
        print('Hello', str(magician).title() , 'i love your magic show'.title())

def main():
    magicians = ['david blaine', 'harry houdini' , 'chris angel']
    show_magicians(magicians)
if(__name__=='__main__'):
    main()