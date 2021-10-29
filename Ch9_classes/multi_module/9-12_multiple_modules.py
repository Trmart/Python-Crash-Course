# 9-12. Multiple Modules: Store the User class in one module, and store the 
# Privileges and Admin classes in a separate module. In a separate file, create 
# an Admin instance and call show_privileges() to show that everything is still 
# working correctly.

from admin import Admin

def main():
    """main"""
    user1 = Admin('trmart','taylor', 'martin', '27')
    user1.describe_user()
    user1.greet_user()
    user1.admin_privileges.show_privileges()

if(__name__=='__main__'):
    main()