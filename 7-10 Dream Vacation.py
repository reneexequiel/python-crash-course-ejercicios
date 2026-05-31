#se crea un diccionario vacio
respuestas = {}

#se crea una bandera
flag = True

#se crea un ciclo while para realizar la encuesta
while flag:
    #se crea 2 variables para realizar la encuesta
    nombre = input("Cual es tu nombre??: ")
    pregunta =input("Que lugares le gustaria visitar en sus vacaciones?: ")

    #almacenamos la respuesta en el diccionario vacio
    respuestas[nombre] = pregunta

    #preguntamos si quiere seguin con la encuesta
    repetir = input("Te gustaria respetir la encuesta? (si/no)")
    if repetir == "no":
        flag = False

    #la encuesta esta completa, se muestra los resultados usando un cliclo for para iterar
    print("\n")
    print("\t----------RESULTADOS-----------")
    print("\n")
    for nombre, pregunta in respuestas.items():
        print("a " + nombre.title() + " le gustaria estar en " + pregunta.title() + ".")