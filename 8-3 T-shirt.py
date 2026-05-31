

def make_shirt(size, message):
    print("la polera roja es de talla", size, "y su estampado dice", message)
make_shirt('s', 'hola mundo')


#misma funcion pero con keywords

def make_shirt(size, message='me gusta programar en fedora'):
    print("la polera negra es de talla", size.title(), "y su estampado dice:", message)
make_shirt(size='s')