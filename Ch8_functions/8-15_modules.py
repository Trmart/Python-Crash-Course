
import user_profile
def main():
    user = user_profile.build_profile('taylor','martin', major = 'Computer Science', minor = 'math', hobby = 'playing guitar')
    for key, val in user.items():
        print(str(key +':' +val).title())

if(__name__ == '__main__'):
    main()