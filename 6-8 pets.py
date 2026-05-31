chico = {
    "nombre": "Thor",
    "apellido": "xxx",
    "edad": 4,
    "sexo": "Masculino",
    "raza":"salchicha",
    "tipo":"perro",
    "nombre dueño":"xxx"
}

agata = {
    "nombre": "Agata",
    "apellido": "Mia",
    "edad": 5,
    "sexo": "Femenino",
    "raza":"mixta",
    "tipo":"perro",
    "nombre dueño":"xxx"
}

kuki = {
    "nombre": "Kuki",
    "apellido": "Mia",
    "edad": 14,
    "sexo": "Femenino",
    "raza":"mixta",
    "tipo":"perro",
    "nombre dueño":"xxx"
}

pola = {
    "nombre": "Pola",
    "apellido": "Andueza",
    "edad": 7,
    "sexo": "Femenino",
    "raza":"mixta",
    "tipo":"gato",
    "nombre dueño":"xxx"
}

mascotas = [thor, agata, kuki, pola]

for mascota in mascotas:
    print(mascota["nombre"] + " " + mascota["apellido"] + " tiene", mascota["edad"], "años y es de sexo " + mascota["sexo"] + " y su dueño es " + mascota["nombre dueño"])   
