
from name_function import get_formatted_name

print("Presiona 'q' en cualquier momento para salir del programa")


while True:
    first = input("Ingresa tu primer nombre: ")
    if first == 'q':
        break
    last = input("Ingresa tu apellido: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\tNombre pulcramente formateado: " + formatted_name + '.')
