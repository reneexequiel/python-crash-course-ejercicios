






bandera = True
while bandera:
    mensaje = str(input("ingresa un aderezo para agregar a tu pizza"))

    if mensaje == "salir":
        print("programa finalizado")
        break
    else:
        print("Tu pizza tendra los siguientes aderezos: ", mensaje)