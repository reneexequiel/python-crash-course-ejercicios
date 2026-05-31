#archivo: ejercicio.py
#autor: rene marambio
#fecha: 18-02-24
#descripcion: script para ejercitar manejar los errores y excepciones.
#nota: puede haber la cantidad que sea de declaraciones except, en un bloque try.
#nota 2: se puede usar la declaracion 'Exception' en except para manipular errores de modo general.

# except ZeroDivisionError:
 
# try:
#     dividendo = input("Ingresa un numero entero: ")
#     divisor = input("Ingresa otro numero entero: ")
#     respuesta = int(dividendo) / int(divisor)
#     print("El resultado es: ",  respuesta)
# except ZeroDivisionError:
#     print("No se puede dividir un numero entre 0")

#ValueError: Indica un error de tipo valor inapropiado
#TypeError: Indica un error de tipo en una operación.

# try:
#     x = int(input("ingresa un numero entero: "))
#     print("El numero ingresado es ", x)

# except TypeError:
#     print("Solo se puede concatenar cadenas a cadenas, no cadenas a numeros.")

# except ValueError:
#     print("Ha habido una excepcion, revisa bien el codigo.")


#NameError: indica que se esta intentando utilizar una variable que no existe.
# try:
#     a = 5
#     print(A)
# except NameError:
#      print("Hay un error de NOMBRE en el codigo.")
# except Exception:
#     print("Sigue habiendo un error en el codigo")

#AttributeError: Indica que un objeto no tiene un atributo.
# class Dog:
#     def __init__(self, pelo):
#         self.pelo = pelo
# objeto = Dog("rubio")

# try:
#     print(objeto.objeto_inexistente)
# except AttributeError:
#     print("El atributo para el objeto no existe.")


#IdexError: Indica que un indice esta fuera de rango
# try:
#     x = [1,2,3,4,5]
#     print(x[6])
# except IndexError:
#         print("Hay un error de rango en la lista.")

#KeyError: Indica que una clave no está presente en un diccionario.
# try:
#     diccionario = {1: "uno", 2: "dos", 3:"tres"}
#     print(diccionario[4])
# except KeyError:
#     print("No hay valor asignado a la llave.")