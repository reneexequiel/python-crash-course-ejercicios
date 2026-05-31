#se crea una lista con algunos elementos
sandwich_orders = ['Sandwich de jamon y queso', 'Sandwich de pollo', 'Sandwich de pavo', 
                   'Sandwich de club', 'sandwich de atun','pastrami']

#se crea una lista vacia
finished_sandwiches = []

#se crea un bucle while para iterar en la lista compuesta de elementos
while sandwich_orders:
    sandwich_actuales = sandwich_orders.pop()
    print("\nSandwich Pedidos: " + sandwich_actuales.title())
    print("\t---Cocinando---")

    finished_sandwiches.append(sandwich_actuales)
    #print("\tLos siguientes sandwich estan listos: ")

    for finished_sandwich in finished_sandwiches:
        print("\tSandwich terminados: " + finished_sandwich.title())
