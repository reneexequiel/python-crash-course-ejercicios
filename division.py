#Archivo:division.py
#Autor: Rene Marambio
#Fecha: 05-02-24
#Descripcion: crear un script para manipular los try-except-else en python.


# try:
#     print(5/0)

# except ZeroDivisionError:
#     print("No puedes dividir un numero entre 0 ")

# print("Dame 2 numeros y los dividire")
# print("Presiona 'q' para salir")

# bandera = True

# while bandera:
#     first_number = input("\nPrimer numero: ")
#     if first_number == 'q':
#         break
#     second_number = input("\nSegundo numero: ")
#     if second_number == 'q':
#         break
#     try:
#         respuesta = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("NO puedes dividir un nuemro entre 0")
#     else:
#         print(respuesta)