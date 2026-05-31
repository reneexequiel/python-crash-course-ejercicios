class Dog():
    """a simple attempt to model a dog."""

    def __init__(self, name, age):
        """initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over.")


# esta es una instancia de la clase Dog. tiene los atributos nombre y edad, con los valores
# willie y 6. las instancias se utilizan para crear objetos especificos
# que se pueden utilizar en un programa.
my_dog = Dog('willie',6)
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog's age is " + str(my_dog.age) + "years old.")
my_dog.sit()

print("\n")
print("My dog's name is " + your_dog.name.title() + ".")
print("My dog's age is " + str(your_dog.age) + ".")
your_dog.sit()