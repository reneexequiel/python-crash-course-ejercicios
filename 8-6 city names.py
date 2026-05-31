

def city_country(ciudad, pais):
    """se retorna un diccionario con una ciudad y un pais"""
    lugar = {'ciudad':ciudad.title(), 'pais':pais.title()}
    return lugar

x = city_country('santiago', 'chile')
y = city_country('berlin', 'alemania')
z = city_country('tokyo', 'japon')
print(x['ciudad'] + ", " +  x['pais'])
print(y['ciudad'] + ", " +  y['pais'])
print(z['ciudad'] + ", " +  z['pais'])