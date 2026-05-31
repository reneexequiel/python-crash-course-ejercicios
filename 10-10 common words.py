#Archivo: 10-10 common words.py
#Autor: rene marambio
#Fecha: 19-02-24
#Descripcion: crear un script que diga la cantidad de veces que se repite una palabra en un archivo txt.


# def common_words(filename, word):
#     try:
#         with open(filename) as file:
#             contents = file.read()
#     except FileNotFoundError:
#         pass
#     else:
#         word_count = contents.lower().count(word)
#         print("La palabra ", "-->" ,word, "<--"," aparece ", word_count, " veces en el archivo ", filename, ".")
    
# filename = 'The Great Gatsby.txt'
# common_words(filename,'her')