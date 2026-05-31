
#funcion con tercer parametro opcional
def city_country(city, country, population=''):
    if population:
        full_name = city + ' ' + country + ' ' + population
        return full_name.title()
    else:
        full_name = city + ' ' + country
city_country('santiago', 'chile', '20.000.000')

# #funcion con tercer parametro con numero entero
# def city_country(city, country, population=20000000):
#     if population:
#         full_name = city + ' ' + country + ' ' + population
#         return full_name.title()
#     else:
#         full_name = city + ' ' + country
# city_country('santiago', 'chile', '20.000.000')