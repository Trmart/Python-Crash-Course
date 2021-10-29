# 9-11. Imported Admin: Start with your work from Exercise 9-8 (page 178).
# Store the classes User, Privileges, and Admin in one module. Create a separate file, make an Admin instance, and call show_privileges() to show that 
# everything is working correctly.
import user

def main():
    """main"""
    user1 = user.Privileges('trmart','taylor', 'martin', '27')
    user1.describe_user()
    user1.greet_user()
    user1.show_privileges()

if(__name__=='__main__'):
    main()