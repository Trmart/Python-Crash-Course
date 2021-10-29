from user import User

class Privileges(User):
    def __init__(self, user_name, first_name, last_name, age):
        super().__init__(user_name, first_name, last_name, age)
    privileges = ["can add post", "can delete post", "can ban user","can read files", 'can write files','can execute files','can modify files']

    def show_privileges(self):
        print('user has the following privileges:'.title())
        for privilege in self.privileges:
            print(str(privilege).title())

class Admin(User):
    """This Admin class is a child of the parent class User, inheriting all of its trait and methods"""

    def __init__(self,user_name,first_name,last_name,age):
        super().__init__(user_name,first_name,last_name,age)
        self.admin_privileges = Privileges(user_name,first_name,last_name,age)


