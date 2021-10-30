#word counter program

def count_words(file_name):
    """this function counts the number of words in a file"""
    try:
        with open(file_name,'r') as file_object:
            file_contents = file_object.read()
    except FileNotFoundError:
        print('THE FILE ' + file_name + ' WAS NOT FOUND')
    else:
        words = file_contents.split()
        num_words = len(words)
        print('the file ' + file_name + ' has ' + str(num_words) + ' words in it')

def main():
    """main"""
    count_words('helloworld.txt')
if(__name__=='__main__'):
    main()