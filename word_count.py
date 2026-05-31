

# def count_words(filename):
#     """contar el numero aproximado de palabras de un archivo de texto."""
    

#     try:
#         with open(filename) as file_object:
#             contents = file_object.read()
#     except FileNotFoundError:
#         msg = "Lo sentimos, el archivo " + filename + " no existe."
#         print(msg)
#     else: 
#         #contar el numero aproximado de palabras en un archivo de texto.
#         words = contents.split()
#         num_words = len(words)
#         print("El archivo " + filename + " tiene acerca de " + str(num_words) + " palabras.")

# filenames = ['alice.txt', 'siddhartha.txt', 'mobi_dick.txt', 'little_women.txt']

# for filename in filenames:
#     count_words(filename)


#################  mismo metodo pero esta vez se usa la declaracion 'pass'  #################################

# def count_words(filename):
#     """contar el numero aproximado de palabras de un archivo ed texto."""
    

#     try:
#         with open(filename) as file_object:
#             contents = file_object.read()
#     except FileNotFoundError:
#         pass
#     else: 
#         #contar el numero aproximado de palabras en un archivo de texto.
#         words = contents.split()
#         num_words = len(words)
#         print("El archivo " + filename + " tiene acerca de " + str(num_words) + " palabras.")

# filenames = ['alice.txt', 'siddhartha.txt', 'mobi_dick.txt', 'little_women.txt']

# for filename in filenames:
#     count_words(filename)