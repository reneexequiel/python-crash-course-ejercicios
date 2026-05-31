



prompt = "\n dime algo, y lo repetire"
prompt += "\n ingresa 'salir' para terminar el programa"

# mensaje = ""

# while mensaje != "salir":
#     mensaje = input(prompt)
#     if mensaje != "salir":
#         print(mensaje)



active = True
while active:
    message = input(prompt)

    if message == "quit":
        active = False
    else:
        print(message)