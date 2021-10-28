# 9-8. Privileges: Write a separate Privileges class. The class should have one 
# attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance 
# as an attribute in the Admin class. Create a new instance of Admin and use your 
# method to show its privileges.

class User():
    """Simple User Class that creates a user profile"""

    def __init__(self,user_name,first_name,last_name,age):
        """Initializer to set username, first name, last name, and age"""
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def describe_user(self):
        """Prints Summary of Users Info"""
        print(str('username: '+self.user_name).title())
        print(str('first name: '+self.first_name).title())
        print(str('last name: '+self.last_name).title())
        print(str('age: '+self.age).title())

    def greet_user(self):
        """prints a personalized greeting to user"""
        print(str('greetings ' + self.user_name + ' thank you for logging in again').title())

def main():
    """main"""
    user1 = User('trmart','taylor', 'martin', '27')
    user1.describe_user()
    user1.greet_user()

if(__name__=='__main__'):
    main()