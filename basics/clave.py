# Problema Contraseña
condicional = 'python'
password = input('introduce la contraseña:')
if password == condicional:
    print('Contraseña correcta!')
if password != condicional:
    print('Tienes 2 intento más')
    password = input('introduce la contraseña:')
    if password == condicional:
        print('Contraseña correcta!')
    if password != condicional:
        print('Ultimo intento')
        password = input('introduce la contraseña:')
        if password == condicional:
            print('Contraseña correcta!')
        else:
            print('Error, contraseña incorrecta')