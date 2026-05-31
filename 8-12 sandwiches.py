

def sandwiches(*items):
    for item in items:
        print("\nCreando sandwich con los siguientes aderezos...")
        print("- " + item.title())

sandwiches('tomates', 'papas al hilo', 'lechuga', 'palta')
sandwiches('pepinillo')