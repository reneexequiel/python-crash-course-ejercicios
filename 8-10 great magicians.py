def show_magicians(magos):
    """imprimir la lista de cada mago en la lista"""
    for mago in magos:
        mago = mago.title()
        print(mago)

def make_great(mago):
    """crar una funcion para modificar la lista de magos y agregar la frase 'GREAT' para cada mago"""
    grandes_magos = []

    while magos:
        mago = magos.pop()
        gran_mago = mago + ' the great'
        grandes_magos.append(gran_mago)

    for gran_mago in grandes_magos:
        magos.append(gran_mago)
    
    return magos

magos = ["harry houdini", "David Copperfield", "Criss Angel", "David Blaine", "Dynamo"]
show_magicians(magos)

print("\nGRANDES MAGOS: ")
grandes_magos = make_great(magos[:])
show_magicians(magos)

print("\nMAGOS ORIGINALES: ")
show_magicians(magos)