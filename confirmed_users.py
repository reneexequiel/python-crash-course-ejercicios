

# sourcery skip: use-fstring-for-concatenation
usuarios_no_confirmados = ['alice', 'brian', 'candance']
usuarios_confirmados = []

while usuarios_no_confirmados:
    usuarios_actuales = usuarios_no_confirmados.pop()
    print("usuarios verificados: " + usuarios_actuales.title())

    usuarios_confirmados.append(usuarios_actuales)
    print("los siguientes usuarios han sido confirmados: ")
    
    for usuarios_confirmado in usuarios_confirmados:
        print(usuarios_confirmado.title())