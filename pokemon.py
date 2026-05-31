#Archivo: pokemon.py
#Autor:Rene Marambio
#Fecha: 12-12-2023
#Descripcion: usar las clases, metodos, atributos e instancias para crear un script relacionado con pokemon

class Pokemon():
    #se crea atributos para los pokemon
    def __init__(self, nombre, tipo, hp):
        self.nombre = nombre
        self.tipo = tipo
        self.hp = 0

    #se crea los metodos
    def obtener_nombre(self):
        """retorna el nombre completamente formateado y pulcro"""
        nombre_completo = self.nombre
        return nombre_completo.title()
    
    def obtener_tipo(self):
        """"retorna el tipo del pokemon"""
        nombre_tipo = self.tipo
        return nombre_tipo.title()
    
    def obtener_hp(self):
        """retorna los puntos de vida de un pokemon"""
        cantidad_hp = self.hp
        return cantidad_hp

#se crea la instancia

pikachu = Pokemon('pikachu', 'electrico',0)
pikachu.hp = 60
print(pikachu.nombre.title() + ' ' + 'es de tipo ' + pikachu.tipo.title() + ' y su HP es de',  pikachu.hp)

charmander = Pokemon('charmander', 'fuego', 0)
charmander.hp = 60
print(charmander.nombre.title() + ' ' + 'es de tipo ' + charmander.tipo.title() + ' y su HP es de', charmander.hp)

bulbasour = Pokemon('bulbasour', 'hierva', 0)
bulbasour.hp = 40
print(bulbasour.nombre.title() + ' ' + 'es de tipo ' + bulbasour.tipo.title() + ' y su HP es de', bulbasour.hp)

squirtle = Pokemon('squirtle', 'agua', 0)
squirtle.hp = 40
print(squirtle.nombre.title() + ' ' + 'es de tipo ' + squirtle.tipo.title() + ' y su HP es de', squirtle.hp)