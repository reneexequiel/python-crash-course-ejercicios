## ejercicio 8-15

def print_models(unprinted_designs, completed_models):
    """simular impresiones de cada diseño, hasta que no haya nada en la lista.
    mover cada diseño a la variable completed_models despues de mostrar por pantalla"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        #simular impresiones 3D desde el diseño
        print("Imprimiendo modelos: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """desplegar todos los modelos impresos"""
    print("\nLos siguientes modelos han sido impresos: ")
    for completed_model in completed_models:
        print(completed_model)

