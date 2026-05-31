#archivo: 10-8 cats and dogs.py
#fecha: 14-02-24
#desarrollador: Rene Marambio
#descripcion: script que sirve para leer un archivo txt y mostrar la cantidad de palabras que tiene
#si no existe el archivo este muestra por pantalla que no existe. Todo esto usando try-except. 


# def cats_and_dogs(filename):
#     try:
#         with open(filename) as file_object:
#             contents = file_object.read()

#     except FileNotFoundError:
#         mensaje = "Lo sentimos, el archivo  " + filename + " no existe."
#         print(mensaje)
    
#     else:
#         words = contents.split()
#         num_words = len(words)
#         print("El archivo " + filename + " tiene acerca de " + str(num_words) + " palabras.")



# filenames = ['cats.txt', 'dogs.txt']

# for filename in filenames:
#     cats_and_dogs(filename)

