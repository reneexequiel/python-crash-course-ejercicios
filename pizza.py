

# def make_pizza(*toppings):
#     for topping in toppings:
#         print("\nMaking a pizza with the following toppings: ")
#         print(" -" + topping)

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese', 'jamon', 'queso blanco')


# def make_pizza(size, *toppings):
#     """" resumen de las pizzas que estamos a punto de realizar """""
#     print("\nMaking a " + str(size) + "-inch pizza with the following toppings: ")
#     for topping in toppings:
#         print("- " + topping)

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'jamon', 'queso blanco', 'oregano')


def make_pizza(size, *toppings):
    """" resumen de las pizzas que estamos a punto de realizar """""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)
