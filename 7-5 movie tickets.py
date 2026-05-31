


# sourcery skip: remove-redundant-if
bandera = True
while bandera:
    tickets = input("Ingresa tu edad: ")

    if tickets == "salir":
        print("programa finalizado")
        break
    elif int(tickets) < 3:
        print("Retira el ticket de forma gratuita")
    elif int(tickets) >= 3 and int(tickets) <= 12:
        print("El costo del ticket es de 10 dolares")
    else:
        print("El costo del ticket es de 15 dolares")
