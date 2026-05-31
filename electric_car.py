#Archivo: electric_car.py
#Autor: Rene Marambio 
#Fecha:12-12-2023
#Descripcion: Se reutiliza el codigo del archivo car.py para agregarle herencia.


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

#se crea una nueva clase hijo 
class Battery():
    """un nuevo intento para modelar la bateria para un auto electrico."""
    
    def __init__(self, battery_size=75):
        """se inicializan los atributos de la bateria"""
        self.battery_size = battery_size

    #se crea un metodo para la bateria
    def describe_battery(self):
        """imprimir la descripción de la bateria"""
        print("Este auto tiene " + str(self.battery_size) + "-KWH de bateria.")

    def get_range(self):
        """imprimir una declaracion acerca del rango de esta bateria"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        message = "Este auto puede ir apropiadamente con " + str(range)
        message += " millas con la carga full"
        print(message)

    def upgrade_battery(self):
        if self.battery_size == 75:
            self.battery_size = 100
            print("actualizada la bateria a 100 kwh")

#se crea una nueva clase hijo
class ElectricCar(Car):
    """representa los aspectos de un auto, especificamente de uno electrico"""

    def __init__(self, make, model, year):
        """inicializar atributos desde la clase padre"""
        super().__init__(make, model, year)
        self.battery = Battery()

print("hacer un auto electrico y checkear el rango:")
my_tesla = ElectricCar('tesla', 'model s', '2016')
#print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
