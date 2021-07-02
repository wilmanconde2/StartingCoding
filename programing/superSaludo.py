# super saludo
# se cambia el orden de las condiciones y el valor por defecto y trabaja normal
hora = int(input('introduce hora militar (0-24) '))
if hora >= 18 and hora <= 24:
    print('Buenas noches')
elif hora >= 0 and hora < 12:
    print('Buenos días')
elif hora >= 12 and hora < 18:
    print('Buenas tardes')
else:
    print('Error')