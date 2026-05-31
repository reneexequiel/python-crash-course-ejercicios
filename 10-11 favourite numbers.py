#archivo: 10-11 favourite_numbers.py
#fecha:06-02-24
#autor: Rene Marambio
#description: script que solicita al usuario su numero favorito, el programa tiene que crear un archivo json 
#y mostrar ese numero en ese archivo json.



import json

def favourite_numbers():
    numero = int(input("Ingresa un numero: "))
    filename = 'numbers.json'

    try:
        with open(filename, 'w') as f:
            json.dump(numero, f)
        return numero
    except Exception:
        return None
    
    
favourite_numbers()