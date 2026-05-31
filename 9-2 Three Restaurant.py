#Archivo: Three Restaurant.py
#Autor: Rene Marambio Andueza
#Fecha:28-11-2023
#Descripcion: Ejercicio 9-2, usar el ejercicio 9-1 para crear multiples instancias.

class Restaurant():
    def __init__(self, name, type):
        #atributos
        self.name = name
        self.type = type
    
    def describe_restaurant(self):
        print(self.name, self.type)

    def open_restaurant(self):
        print("El restaurant esta abierto.")
    
#instancia    
restaurant = Restaurant('ddd', "5 estrellas")
restaurant_republicanos = Restaurant('sss', "4,7 estrellas")
restaurant_alborada = Restaurant('qqq', "4,2 estrellas")
restaurant_akwa = Restaurant('zzz', "4,1 estrellas")

#imprimiendo las instancias
print(restaurant.name.title() + " es un restaurant gourmet")
print(restaurant_republicanos.name.title() + " es un restaurant con una fuente de soda")
print(restaurant_alborada.name.title() + " es un restaurant gourmet")
print(restaurant_akwa.name.title() + " es un restaurant gourmet")
print("\n")

#llamando al metodo
restaurant.describe_restaurant()
restaurant.open_restaurant()
print("\n")
#llamando al metodo restaurarnt republicanos
restaurant_republicanos.describe_restaurant()
restaurant_republicanos.open_restaurant()
