# 9-7. Admin: An administrator is a special kind of user. Write a class called 
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 166) 
# or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list 
# of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of 
# privileges. Create an instance of Admin, and call your method.

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

class Admin(User):
    """This Admin class is a child of the parent class User, inheriting all of its trait and methods"""

    def __init__(self,user_name,first_name,last_name,age):
        super().__init__(user_name,first_name,last_name,age)
    """admin_privileges is a list of privileges that only Admin users can have"""
    admin_privileges = ["can add post", "can delete post", "can ban user","can read files", 'can write files','can execute files','can modify files']

    def show_privileges(self):
        print('admin user has the following privileges:'.title())
        for privilege in self.admin_privileges:
            print(str(privilege).title())
def main():
    """main"""
    user1 = Admin('trmart','taylor', 'martin', '27')
    user1.describe_user()
    user1.greet_user()
    user1.show_privileges()

if(__name__=='__main__'):
    main()