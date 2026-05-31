
def make_album(artista, album, canciones=0):
    """crear un diccionario que contenga informacion de un album y su artista"""
    descripcion = {

        'artista':artista.title(),
        'album':album.title()
                }
    if canciones:
        descripcion['canciones'] = canciones
    return descripcion

while True:
    print("(Presiona 'q' para salir)")

    xartista = input('ingresa el nombre del artista: ')
    if xartista == 'q':
        break

    yalbum = input('ingresa el nombre del album: ')
    if yalbum == 'q':
        break

    z = make_album(xartista, yalbum)
    print(z)