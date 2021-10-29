# 10-2 Replace: uses replace to find a instance of a substr within a string 
# and replaces it with a given word

def main():
    """main"""

    file_name = 'helloworld.txt'

    """Printing file contents by storing 
        the lines in a list and then working with them outside the with block"""
    
    with open(file_name,'r') as file_object:
        lines = file_object.readlines()
    
    line_str = ''
    
    for line in lines:
        line_str += line
    
    print(line_str.replace('Python','C'))

if(__name__=='__main__'):
    main()