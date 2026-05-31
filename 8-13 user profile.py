

def build_profile(first, last, genero,**user_info):
    """Construyendo un diccionario que contenga todo lo relacionado con un usuario"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    profile['genero'] = genero
    
    #iteramos en el diccionario
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Rene', 'Marambio', 'masculino',edad=xx,location='xxxx', 
                            field='Informatica y Finanzas', email='xxxx.xxxx@gmail.com', 
                            telefono='+569-xxx-xxx-xx')
print(user_profile)
