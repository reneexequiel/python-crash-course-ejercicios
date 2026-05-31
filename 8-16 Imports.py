#Archivo: imports.py
#Autor: Rene Marambio Andueza
#Fecha:21-11-2023
#Descripcion: ejercicio 8-16, usando el archivo pets.py,  
#este programa trata de usar la declaracion import para importar modulos,
#funciones y usar alias desde el archivo pets.py.

import pets
from pets import describe_pets
from pets import describe_pets as dp
import pets as p
from pets import *

describe_pets(animal_type='hamster', pet_name='harry')
describe_pets(pet_name='harry', animal_type='hamster')