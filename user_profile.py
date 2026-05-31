

def buildi_profile(first, last, **user_info):
    """Construyendo un diccionario que contenga todo lo relacionado con un usuario"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last

    #iteramos en el diccionario
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = buildi_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)