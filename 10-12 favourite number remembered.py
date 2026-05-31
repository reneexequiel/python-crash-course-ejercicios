
import json


def favourite_numbers():
    
    filename = 'favourite_numbers_rememered.json'
    try:
        with open(filename) as f:
            numero = json.load(f)    
    except FileNotFoundError:
        numero = input("Ingresa un numero: ")
        with open(filename, 'w') as f:
            json.dump(numero, f) 
        print("Gracias, recordare el numero.")
    else:
        print("Yo se cual es tu numero favorito, es: " + str(numero))
    
favourite_numbers()