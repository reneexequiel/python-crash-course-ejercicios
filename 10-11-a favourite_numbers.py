#archivo: 10-11-a favourite_numbers.py
#fecha:06-02-24
#autor: Rene Marambio
#description: script que carga el archivo json 'numbers' para mostrar
#el numero favorito del usuario con un pequeño mensaje



import json

filename = 'numbers.json'

with open(filename, 'r') as f:
    numero = json.load(f)
    print("Tu numero favorito es ---> " + str(numero) + " <---.")