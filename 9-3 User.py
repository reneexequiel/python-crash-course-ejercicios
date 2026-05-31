#Archivo: User.py
#Autor: Rene Marambio Andueza
#Fecha:28-11-2023
#Descripcion: Ejercicio 9-3, se crea un script que sirve para almacenar un perfil de usuario, usando clases, atributos y metodos.

class User():
    def __init__(self, first_name, last_name, edad, genero, campo, email, telefono, direccion, ciudad, pais):
    #se crean los atributos
        self.first_name = first_name
        self.last_name = last_name
        self.edad = edad
        self.genero = genero
        self.campo = campo
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.ciudad = ciudad
        self.pais = pais
        self.login_attempts = 0
    #se crea metodo describe_user
    def describe_user(self):
        print("Informacion del usuario: ")
        print("\t", "-Nombre:",self.first_name)
        print("\t", "-Apellido:",self.last_name)
        print("\t", "-Edad:",self.edad)
        print("\t", "-Genero:",self.genero)
        print("\t", "-Campo:",self.campo)
        print("\t", "-Email:",self.email)
        print("\t", "-Telefono:",self.telefono)
        print("\t","-Direccion:", self.direccion)
        print("\t", "-Ciudad:",self.ciudad)
        print("\t", "-Pais:",self.pais)
    #se crea metodo greet_user
    def greet_user(self):
        print("Hola soy, " + self.first_name + " " + self.last_name + " y les mando un saludo.")
    
    def increment_login_attemps(self):
        self.login_attempts += 1
    
    def reset_login_attemps(self):
        self.login_attempts = 0

#se crea una nueva subclase hijo que hereda de la clase padre User 
class Admin(User):
    #se crea un nuevo atributo
    def __init__(self,first_name, last_name, edad, genero, campo, email, telefono, direccion, ciudad, pais):
        super().__init__(first_name, last_name, edad, genero, campo, email, telefono, direccion, ciudad, pais)
        self.privileges = Privileges()
    

class Privileges():

    def __init__(self, privileges=[]):
        self.privileges = privileges
        
    def show_privileges(self):
        print("Privilegios")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- Este usuario no tiene privilegios")

#se crea instancias
usuario_kelo = Admin("Rene", "Marambio", "34 años", "Masculino", "Finanzas y Tecnologia", 
               "rene.marambio@gmail.com", "+569-660-344-42", "Arica", "Rio yelcho #3841", "Chile")

#llamando instancias con sus metodos
usuario_kelo.describe_user()
usuario_kelo.privileges.show_privileges()

#se crea una nueva instancia con los privilegios de los usuarios
print("\nAgregando privilegios...")
usuario_kelo_privileges = [
    'puede resetear la contraseña',
    'puede moderar discusiones',
    'puede suspender cuentas'
    ]

usuario_kelo.privileges.privileges = usuario_kelo_privileges
usuario_kelo.privileges.show_privileges()

# usuario_pamela = User("Pamela", "Marambio", "38 años", "Femenino", "Finanzas y contabilidad", 
#                "pama.audiconsult@gmail.com", "+569-999-999-99", "Arica", "Rio yelcho #3837", "Chile")

# usuario_mama = User("Marisol", "Andueza", "60 años", "Femenino", "Mantencion y aseo", 
#                "marisol.cachorrita@gmail.com", "+569-888-888-88", "Arica", "Rio yelcho #3837", "Chile")

# usuario_papa = User("Rene Antonio", "Marambio", "62 años", "Masculino", "Seguridad", 
#                "rene.marambio.andueza@gmail.com", "+569-777-777-77", "Arica", "Rio yelcho #3841", "Chile")


# usuario_pamela.describe_user()
# usuario_mama.describe_user()
# usuario_papa.describe_user()
# print("\n")
usuario_kelo.greet_user()
# usuario_papa.greet_user()
# usuario_mama.greet_user()
# usuario_pamela.greet_user()



