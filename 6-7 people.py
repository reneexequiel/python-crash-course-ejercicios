

persona1 = {
    "nombre": "Juan",
    "apellido":"martinez",
    "edad": 25,
    "sexo": "Masculino"

}

persona2 = {
    "nombre": "Pedro",
    "apellido":"lopez",
    "edad": 30,
    "sexo": "Masculino"
}

persona3 = {
    "nombre": "Maria",
    "apellido":"soto",
    "edad": 25,
    "sexo": "Femenino"
}

personas = [persona1, persona2, persona3]

for persona in personas:
    print(persona["nombre"] + " " + persona["apellido"] + " tiene", persona["edad"], "años y es de sexo " + persona["sexo"])