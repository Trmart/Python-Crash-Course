"""user.py is a module created to hold the classes user, admin, and privileges"""

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
        print()

    def greet_user(self):
        """prints a personalized greeting to user"""
        print(str('greetings ' + self.user_name + ' thank you for logging in again').title())
        print()

class Privileges(User):
    def __init__(self, user_name, first_name, last_name, age):
        super().__init__(user_name, first_name, last_name, age)
    privileges = ["can add post", "can delete post", "can ban user","can read files", 'can write files','can execute files','can modify files']

    def show_privileges(self):
        print('user has the following privileges:'.title())
        for privilege in self.privileges:
            print(str(privilege).title())