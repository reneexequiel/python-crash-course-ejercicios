
from Printing_Functions import print_models, show_completed_models

# # iniciar con algunos diseños que necesitan ser impresos
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# #simular impresiones de cada diseño, hasta que no haya nada en la lista
# #mover cada diseño a la variable completed_models despues de mostrar por pantalla
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     #simular impresiones 3D desde el diseño
#     print("printing model " + current_design)
#     completed_models.append(current_design)
# #desplegar todos los modelos impresos
# print("\nThe following models hace been printed: ")
# for completed_model in completed_models:
#     print(completed_model)


#mismo metodo pero usando funciones


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []


print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
