# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the 
# text of a message that should be printed on the shirt. The function should print 
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the 
# function a second time using keyword arguments.

def make_shirt(shirt_size, shirt_text):
    print('we are completeing your order of a '.title() + str(shirt_size).title() + ' t-shirt with the message: '.title() + str(shirt_text).title())

def main():
    make_shirt('large', 'Python Is Awesome!')
    make_shirt(shirt_size='small', shirt_text='java sucks'.title())

if(__name__ == '__main__'):
    main() 