# 8-13. User Profile: Start with a copy of user_profile.py from page 153. Build 
# a profile of yourself by calling build_profile(), using your first and last names 
# and three other key-value pairs that describe you.
def build_profile(first_name,last_name, **user_info):
    user = {}
    user['first name'] = first_name
    user['last name'] = last_name
    for key, val in user_info.items():
        user[key] = val
    return user

def main():
    user = build_profile('taylor','martin', major = 'Computer Science', minor = 'math', hobby = 'playing guitar')
    for key, val in user.items():
        print(str(key +':' +val).title())

if(__name__ == '__main__'):
    main()