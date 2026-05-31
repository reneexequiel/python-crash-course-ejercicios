



from random import randint

#se crea clase die que tiene 1 atributo
class Die():
    def __init__(self, sides=6):
        self.sides = sides
    #se crea un metodo que lanzara un numero aleatorio entre 1 al 6
    def roll_die(self):
        return randint(1, self.sides)

# se crea la instancia
x6 = Die()
#se llama la instancia con su metodo
#x6.roll_die()

#se crea ua lista para almacenar los resultados de 6 tiradas
resultados = []

for elemento in range(10):
    resultado = x6.roll_die()
    resultados.append(resultado)
print(resultados)