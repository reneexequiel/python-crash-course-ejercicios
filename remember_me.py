
import json


def get_stored_username():
    """greet user by name"""
    filename = 'username.json'

    try:
        with open(filename) as f:
            username = json.load(f)
    except Exception:
        return None
    else:
        return username
    
get_stored_username()

def get_new_username():
    """prompt for a new username."""
    username = input('Enter username')
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print("welcome back, " + username + "!.")
    else:
        username = get_new_username()
        filename = 'username.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
            print("welcome back, " + username + "!.")
greet_user()