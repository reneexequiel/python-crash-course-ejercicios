# sourcery skip: use-fstring-for-concatenation
responses = {}

#configurar la bandera para indicar que la encuesta esta activa.
polling_active = True

while polling_active:
    #avisar por el nombre de la persona y su respuesta
    name = input("\nCual es tu nombre?")
    response = input("que montaña le gustaria escalar algun dia?")

    #almacenamos la respuesta en un diccionario
    responses[name] = response

    #descubrimos si alguien mas esta tomando la encuesta
    repeat = input("Te gustaria que otra persona respondiera?) (yes/no)")
    if repeat == 'no':
        polling_active = False

    #la encuesta esta completa. mostrar los resultados
    print("\n---Resultados de la encuesta ---")
    for name, response in responses.items():
        print("a " + name.title() + " le gustaria escalar " + response.title() + ".")