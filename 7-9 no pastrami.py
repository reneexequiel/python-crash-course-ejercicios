#se crea una lista con algunos elementos
sandwich_orders = ['Sandwich de jamon y queso', 'pastrami','Sandwich de pollo', 'Sandwich de pavo', 
                   'Sandwich de club', 'pastrami','sandwich de atun', 'pastrami']

#se crea una lista vacia
finished_sandwiches = []

#se crea un ciclo while para eliminar el sandwich de pastrami
print('Lo sentimos pero nos hemos quedado sin pastrami')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print("\n")

#se crea un bucle while para iterar en la lista compuesta de elementos
while sandwich_orders:
    sandwich_actuales = sandwich_orders.pop()
    print("\nSandwich Pedidos: " + sandwich_actuales.title())
    print("\t---Cocinando---")

    finished_sandwiches.append(sandwich_actuales)
    
#se crea un ciclo for para iterar en la lista de sandwich_orders
print("\n")
for finished_sandwich in finished_sandwiches:
    print("Sandwich terminados: " + finished_sandwich.title())

