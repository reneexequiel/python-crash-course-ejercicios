#Archivo:addition.py
#Autor: Rene Marambio
#Fecha: 13-02-24
#Descripcion: Solicitar al usuario 2 numeros enteros, estos se deben sumar y 
#mostrar el resultado. Si el usuario ingresa una letra o palabra hay que 
#captuar el error y mostrar un mensaje que no se puede usar letras o palabras.



# bandera =  True
# while bandera:
#     valor1 = input("Ingresa un numero entero: ")
#     if valor1 == 'q':
#         for i in range(1):
#             print(chr(10))
#             print("------Programa Terminado------")
#         break

#     valor2 = input("Ingresa otro numero entero: ")
#     if valor2 == 'q':
#         for i in range(1):
#             print(chr(10))
#             print("------Programa Terminado------")
#         break

#     try:
#         respuesta = int(valor1) + int(valor2)            
#     except ValueError:
#         print("No se puede sumar un numero entero con una letra y/o palabra.")        
#     else:
#         print(respuesta)