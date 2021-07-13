# saludo
name = input('Cual es tu nombre?\n-> ')
time = input('Que hora es? (horario militar 0-24)\n-> ')      
if time.isnumeric():
    time = float(time)
    if time >= 0 and time < 12:
        print(f'Buenos días {name.capitalize()}\n')
    elif time >= 12 and time < 18:
        print(f'Buenas tardes {name.capitalize()}\n')
    elif time >= 18 and time <= 24:
        print(f'Buenas noches {name.capitalize()}\n')
    else:
        print('Error de horario')
else:
    print('Error de horario')