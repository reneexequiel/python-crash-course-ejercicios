#archivo: 10-9 silent cats and dogs.py
#fecha: 14-02-24
#desarrollador: Rene Marambio
#descripcion: script que sirve para leer un archivo txt y mostrar la cantidad de palabras que tiene
#si no existe el archivo este muestra por pantalla que no existe. Todo esto usando try-except y la declaracion pass.


def cats_and_dogs(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()

    except FileNotFoundError:
        pass
    
    else:
        words = contents.split()
        num_words = len(words)
        print("El archivo " + filename + " tiene acerca de " + str(num_words) + " palabras.")



filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    cats_and_dogs(filename)