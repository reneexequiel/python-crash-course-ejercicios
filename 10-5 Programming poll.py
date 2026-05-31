#Archivo: programming poll.py
#Autor: Rene Marambio
#Fecha: 02-02-24
#Descripcion: crear un script en python que le pregunte al usuario del porque le gusta programar.


#se crea bandera
bandera = True
#se crea variable que contendra el archivo de texto responses.txt
filename = 'responses.txt'

#se crea ciclo while para preguntar al usuario
while bandera:
    with open(filename, 'a') as file_object:
        file_object.write('\n' + 'Dame una razon del porque te gusta programar en python: ')
        respuesta = input("Razon: ")
        file_object.write('\n' + '\t' + respuesta.title())

## metodo 2: un poco mas sofisticado

# # Se crea bandera
# bandera = True

# # Se crea variable que contendrá el archivo de texto responses.txt
# filename = 'responses.txt'

# # Se crea ciclo while para preguntar al usuario
# while bandera:
#     with open(filename, 'a') as file_object:
#         file_object.write('\n' + 'Dame una razón del porqué te gusta programar en Python: ')
#         respuesta = input("Razon: ")
#         file_object.write('\n' + '\t' + respuesta)

#     # Preguntar al usuario si desea agregar más respuestas
#     continuar = input("¿Quieres agregar otra respuesta? (s/n): ")
    
#     # Si la respuesta no es 's', la bandera se establece en False y se sale del bucle
#     if continuar.lower() != 's':
#         bandera = False

# print("¡Gracias por tus respuestas!")
