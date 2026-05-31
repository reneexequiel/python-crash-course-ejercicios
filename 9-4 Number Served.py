#Archivo: 9-4 Number Served.py
#Autor: Rene Marambio Andueza
#Fecha:01-12-2023
#Descripcion: modificar el ejercicio 9-1, para crear metodos, y modificar instancias.

class Restaurant():
    def __init__(self, name, type, number_served):
        
        self.name = name
        self.type = type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(self.name, self.type)

    def open_restaurant(self):
        print("El restaurant esta abierto.")
    #se crea metodo para Permitir al usuario establecer la cantidad de clientes que han sido atendidos.
    def set_number_served(self, number_served):
        self.number_served = number_served
    #se crea el metodo para incrementar el numero de clientes atendidos.
    def increment_number_served(self, additional_served):
        self.number_served += additional_served

#instancia    
restaurant = Restaurant('rayu', 'gourmet',10)

#llamando al metodo
restaurant.describe_restaurant()
restaurant.open_restaurant()

#imprimiendo instancia con valor 430
print(f"\nNumeros atendidos:  {restaurant.number_served}")
restaurant.number_served = 430
print(f"El numero de clientes que han sido atendidos son: {restaurant.number_served}")

#imprimiendo instancia con distinto valor
restaurant.set_number_served(1000)
print(f"Numeros atendidos: {restaurant.number_served}")

#imprimiendo instancia con incremento de atenciones.
restaurant.increment_number_served(200)
print(f"Numeros atendidos: {restaurant.number_served}")
print("\n")
