#Archivo: Login Attemps.py
#Autor: Rene Marambio 
#Fecha:06-12-2023
#Descripcion: Ejercicio 9-5, se reutiliza el codigo del ejercicio 9-3 para agregar atributos, metodos, etc.

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

    #se crea un metodo para configurar los intentos de acceso.
    def set_login_attempts(self, login_attempts):
        self.login_attempts = login_attempts

    #se crea un metodo para aumentar los intentos de acceso.
    def increment_login_attempts(self):
        self.login_attempts += 1

    #se crea un metodo para resetear los intentos de acceso a 0.
    def reset_login_attempts(self):
        self.login_attempts = 0

#se crea instancias
usuario_kelo = User("Rene", "Marambio", "xx años", "Masculino", "Finanzas y Tecnologia", 
               "ñññ.ñññ@uuu.com", "+56111-111-11", "Arica", "kkk", "ñññ")


#se crea instancia para aumentar logins
print("Haciendo 3 intentos de login")
usuario_kelo.increment_login_attempts()
usuario_kelo.increment_login_attempts()
usuario_kelo.increment_login_attempts()
print(f" Intentos de logins: {usuario_kelo.login_attempts}")


print("\nReseteando intentos de login...")
usuario_kelo.reset_login_attempts()
print(f" Intentos de login: {usuario_kelo.login_attempts}")


