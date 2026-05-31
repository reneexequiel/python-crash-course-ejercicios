#Archivo: CLASS_restaurant.py
#Autor: Rene Marambio Andueza
#Fecha:24-11-2023
#Descripcion: ejercicio 9-1, crear un archivo CLASS_restaurant, para aprender sobre las clases en python  


class Restaurant():
    def __init__(self, name, type):
        
        self.name = name
        self.type = type
    
    def describe_restaurant(self):
        print(self.name, self.type)

    def open_restaurant(self):
        print("El restaurant esta abierto.")

#se crea una nueva clase hijo
class IceCreamStand(Restaurant):
    #se crea un nuevo atributo
    def __init__(self, name, type='ice_cream'):
        super().__init__(name, type)
        self.flavors = []

    #se crea un nuevo metodo para mostrar los sabores iterando en una lista
    def display_flavors(self):
        print("Sabores disponibles: ")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")
        
helado = IceCreamStand('Helado grande')
helado.flavors = ['vainilla', 'chocolate', 'orange','fresa', 'galleta y crema']
helado.display_flavors()
    
    

#instancia    
#restaurant = Restaurant('RAYU', '5 estrellas')
#imprimiendo la informacion del restaurant
#print("El resturant " + restaurant.name.title() + " esta abierto. ")
#llamando al metodo
#restaurant.describe_restaurant()
#restaurant.open_restaurant()