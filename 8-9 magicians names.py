def show_magicians(names):
    """pasar la lista de magos a una funcion, la funcion deberia mostrar por pantalla el nombre de cada mago"""
    for name in names:
        mago = name.title()
        print(mago)

lista = ["harry houdini", "David Copperfield", "Criss Angel", "David Blaine", "Dynamo"]
show_magicians(lista)