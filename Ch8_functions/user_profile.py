"""This Module user_profile creates a method to build a user profile.
    build_profile takes three parameters build_profile(first name, last name, an arbitrary number of keys and values )
    Then creates and returns a dictionary filled with the sent in arguments"""
def build_profile(first_name,last_name, **user_info):
    user = {}
    user['first name'] = first_name
    user['last name'] = last_name
    for key, val in user_info.items():
        user[key] = val
    return user