# 8-2. Favorite Book: Write a function called favorite_book() that accepts one 
# parameter, title. The function should print a message, such as One of my 
# favorite books is Alice in Wonderland. Call the function, making sure to 
# include a book title as an argument in the function call.

"""Def fav_book() is a function prototype that accepts a string parameter and displays it to the console"""
#above is an example of a docsting in Python, it is enclosed in triple quotes and describes what a function does. 
def fav_book(book_title):
    print('one of my favorite books is '.title() + book_title + '!\n')

def main():
    book = input('please enter one of your favorite book titles: '.title())
    fav_book(book)

if(__name__ == '__main__'):
    main()