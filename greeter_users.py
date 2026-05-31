

def greet_users(names):
    """imprimir un saludo simple a cada usuario en la lista"""
    for name in names:
        msg = "hola, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'type', ' margot']
greet_users(usernames)