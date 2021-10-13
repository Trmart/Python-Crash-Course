# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large 
# by default with a message that reads I love Python. Make a large shirt and a 
# medium shirt with the default message, and a shirt of any size with a different 
# message.

def make_shirt(shirt_text, shirt_size = 'LG'):
    print('we are completeing your order of a '.title() + str(shirt_size).title() + ' t-shirt with the message: '.title() + str(shirt_text).title())

def main():
    make_shirt('I Love Python!')
    make_shirt(shirt_text='I Love Python!', shirt_size = 'MED')
    make_shirt(shirt_text= 'Java Sucks' , shirt_size='SM')

if(__name__ == '__main__'):
    main() 