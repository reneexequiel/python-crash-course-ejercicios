#Archivo: car.py
#Autor: Rene Marambio Andueza
#Fecha:01-12-2023
#Descripcion: Se crea un script para modificar atributos a traves de los metodos.


class Car():
    #se crean atributos
    def __init__(self, make, model, year):
        """Iniciar atributos para describir un auto"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
        #se crea el metodo
    def get_descriptive_name(self):
        """retorna el nombre completamente formateado y pulcro."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Mostrar por pantalla el kilometraje del auto."""
        print("Este auto tiene " + str(self.odometer_reading) + " kilometros.")
    
    def update_odometer(self, mileage):
        """configurar el cuenta-kilometros leyendo los valores dados"""
        """Rechace la oportunidad si intenta hacer retroceder el odómetro."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("No puedes retroceder el cuenta-kilometrage")

    def increment_odometer(self, miles):
        """sume la cantidad dada a la lectura del odómetro."""
        self.odometer_reading += miles

my_user_car = Car('subaru', 'outback', '2013')
print(my_user_car.get_descriptive_name())

my_user_car.update_odometer(23500)
my_user_car.read_odometer()

my_user_car.increment_odometer(100)
my_user_car.read_odometer()

# #se crea la instancia    
# my_new_car = Car('audi', 'a4', '2016')
# # my_new_car.odometer_reading = 23

# #se llama el metodo update_odometer y read_odometer
# my_new_car.update_odometer(2)
# my_new_car.read_odometer()

# #se muestra por pantalla la instancia con su respectivo metodo.
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()