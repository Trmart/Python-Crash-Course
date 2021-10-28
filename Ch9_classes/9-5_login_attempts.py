# 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 166). Write a method called increment_
# login_attempts() that increments the value of login_attempts by 1. Write 
# another method called reset_login_attempts() that resets the value of login_
# attempts to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented 
# properly, and then call reset_login_attempts(). Print login_attempts again to 
# make sure it was reset to 0.

class User():
    """Simple User Class that creates a user profile"""

    def __init__(self,user_name,first_name,last_name,age):
        """Initializer to set username, first name, last name, and age"""
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0
    
    def describe_user(self):
        """Prints Summary of Users Info"""
        print(str('username: '+self.user_name).title())
        print(str('first name: '+self.first_name).title())
        print(str('last name: '+self.last_name).title())
        print(str('age: '+self.age).title())

    def greet_user(self):
        """prints a personalized greeting to user"""
        print(str('greetings ' + self.user_name + ' thank you for logging in again').title())
    
    def increment_login_attempt(self):
        """Increments users number of login attempts by 1"""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """rests users number of login attempts"""
        self.login_attempts=0
    
    def print_login_attempts(self):
        """prints the users number of login attempts"""
        print('number of login attempts: '.title() + str(self.login_attempts).title())
    
def main():
    """main"""
    user1 = User('trmart','taylor', 'martin', '27')
    user1.describe_user()
    user1.greet_user()
    user1.print_login_attempts()

    user1.increment_login_attempt()
    user1.increment_login_attempt()
    user1.increment_login_attempt()
    user1.increment_login_attempt()

    user1.print_login_attempts()

    user1.reset_login_attempts()
    user1.print_login_attempts()

if(__name__=='__main__'):
    main()