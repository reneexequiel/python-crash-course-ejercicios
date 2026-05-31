

def describe_city(city, pais='chile'):
    mensaje = city.title() + ' se encuentra en ' + pais.title()
    print(mensaje)
describe_city('arica')
describe_city('puerto varas')
describe_city('berlin', 'alemania')