


def make_album(artista, album, canciones=0):
    """crear un diccionario que contenga informacion de un album y su artista"""
    descripcion = {

        'artista':artista.title(),
        'album':album.title()
                }
    if canciones:
        descripcion['canciones'] = canciones
    return descripcion

depeche_mode = make_album('depeche mode', 'spirit', canciones=17)
print(depeche_mode)

placebo = make_album('placebo', 'sleeping with ghosts')
print(placebo)

jamiroquai = make_album('jamiroquai', 'Dynamite')
print(jamiroquai)