def build_profile(name, lastname, **user_info):
    """takes 2 necessary arguments and creates a dictionary with optional user_info data"""
    user_info['name'] = name
    user_info['lastname'] = lastname
    return user_info

