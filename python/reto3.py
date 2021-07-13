import numpy as np
import sys

print('''
________  __            __    __             __             ______                                 
|        \|  \          |  \  |  \           |  \           /      \                                
\$$$$$$$$ \$$  _______ | $$\ | $$  ______  _| $$_         |  $$$$$$\  ______    ______    ______   
    | $$   |  \ /       \| $$$\| $$ /      \|   $$ \        | $$   \$$ /      \  /      \  /      \  
    | $$   | $$|  $$$$$$$| $$$$\ $$|  $$$$$$\ \$$$$$$       | $$      |  $$$$$$\|  $$$$$$\|  $$$$$$\ 
    | $$   | $$| $$      | $$\$$ $$| $$    $$ | $$ __       | $$   __ | $$  | $$| $$   \$$| $$  | $$ 
    | $$   | $$| $$_____ | $$ \$$$$| $$$$$$$$ | $$|  \      | $$__/  \| $$__/ $$| $$      | $$__/ $$ 
    | $$   | $$ \$$     \| $$  \$$$ \$$     \  \$$  $$       \$$    $$ \$$    $$| $$      | $$    $$ 
    \$$    \$$  \$$$$$$$ \$$   \$$  \$$$$$$$   \$$$$         \$$$$$$   \$$$$$$  \$$      | $$$$$$$  
                                                                                        | $$       
                                                                                        | $$       
                                                                                        \$$          
\nBienvenido al sistema de ubicación para zonas públicas WIFI\n     ''')

def saludo():
    print('Ingresa la coordenada WiFi favorita de casa, trabajo y parque\n')

def enter_and_validation_coordinates_home(home=[]):
    while True:
        try:
            home.clear()
            latitude_home = float(input('Ingrese latitud casa\n-> '))
            if -3.002 >= latitude_home >= -4.227:
                home.append(latitude_home)
            else:
                print('Error coordenada')
                sys.exit()
        except ValueError:
            print('Error coordenada')
            sys.exit()
        while True:
            try:
                longitude_home = float(input('Ingrese longitud casa\n-> '))
                if  -69.714 >= longitude_home >= -70.365:
                    home.append(longitude_home)
                else:
                    print('Error coordenada')
                    sys.exit()
            except ValueError:
                print('Error coordenada')
                sys.exit()
            print(f'Coordenadas WiFi casa {home}\n')
            return home

def enter_and_validation_coordinates_work(work=[]):
    while True:
        try:
            work.clear()
            latitude_work = float(input('Ingrese latitud trabajo\n-> '))
            if -3.002 >= latitude_work >= -4.227:
                work.append(latitude_work)
            else:
                print('Error coordenada')
                sys.exit()
        except ValueError:
            print('Error coordenada')
            sys.exit()
        while True:
            try:
                longitude_work = float(input('Ingrese longitud trabajo\n-> '))
                if  -69.714 >= longitude_work >= -70.365:
                    work.append(longitude_work)
                else:
                    print('Error coordenada')
                    sys.exit()
            except ValueError:
                print('Error coordenada')
                sys.exit()
            print(f'Coordenadas WiFi trabajo {work}\n')
            return work
        
def enter_and_validation_coordinates_park(park=[]):
    while True:
        try:
            park.clear()
            latitude_park = float(input('Ingrese latitud parque\n-> '))
            if -3.002 >= latitude_park >= -4.227:
                park.append(latitude_park)
            else:
                print('Error coordenada')
                sys.exit()
        except ValueError:
            print('Error coordenada')
            sys.exit()
        while True:
            try:
                longitude_park = float(input('Ingrese longitud parque\n-> '))
                if  -69.714 >= longitude_park >= -70.365:
                    park.append(longitude_park)
                else:
                    print('Error coordenada')
                    sys.exit()
            except ValueError:
                print('Error coordenada')
                sys.exit()
            print(f'Coordenadas WiFi parque {park}\n')
            return park
        
def is_list_empty(home, work, park):
    if home == [] or work == [] or park == []:
        print('Error')
        sys.exit()
        
def create_matriz(home, work, park):
    matriz_coordinates = []
    matriz_coordinates.append(home)
    matriz_coordinates.append(work)
    matriz_coordinates.append(park)
    matriz_coordinates = np.array(matriz_coordinates)
    return matriz_coordinates

def good_bye():
    print('''
       ___     ___     ___     ___     ___     ___     ___   
      / __|   | _ \   /   \   / __|   |_ _|   /   \   / __|  
     | (_ |   |   /   | - |  | (__     | |    | - |   \__ \  
      \___|   |_|_\   |_|_|   \___|   |___|   |_|_|   |___/  
    _|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
    "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
    ''')
    
    
# usuario y contrasena predefinidos
user = '51604'
password = '40615'
home = []
work = []
park = []
matriz_coordinates = []
menu = ['Cambiar contraseña','Ingresar coordenadas actuales','Ubicar zona wifi más cercana',
        'Guardar archivo con ubicación cercana','Actualizar registros de zonas wifi desde archivo',
        'Elegir opción de menú favorita','Cerrar sesión']
guess1 = ('Para confirmar por favor responda:\nSe trata de un caso extraño, pues siendo'
          'siempre el mismo, valgo mucho o valgo nada,según el sitio en el que vaya\n-> ')
guess2 = ('Para confirmar por favor responda:\nLas estaciones del año y también los '
          'elementos y los puntos cardinales, ese número represento\n-> ') 
print(f'Usuario {user}')
name = input('Introduzca su usuario\n-> ')  # se pide usuario predefinido
if name != user:
    print('Error')
else:
    print(f'contraseña {password}')
    clave = input('Introduzca su contraseña\n-> ')  # se pide clave predefinida
    if clave != password:
        print('Error')
    else:
        print('CAPTCHA')
        first_num = 604
        second_num = (((6*5)-(5*4))-(4+6))
        add = first_num+second_num              
        response_captcha = int(input(f'{first_num} + {second_num} = '))  # solucionar operación matemática
        if response_captcha != add:
            print('Error')
        else:
            print('\nSesión iniciada\n ')
            for n, m in enumerate(menu,1):
                print(n, m)
            print()
            option = input('Elija una opción\n-> ')
            print('\n'*50)
            counter = 0                # contador iniciado en 0
            while True:
                if option == '1':                                 # menu de opciones escogido 1 - 7
                    counter = 0 
                    print('Usted ha elegido la opción 1\n')
                    confirmation = input('Confirme contrasena actual\n->')
                    if confirmation != password:
                        print('Error')
                        sys.exit() 
                    else:
                        password_new = input('Ingrese su nueva contrasena\n-> ')
                        if password_new == password:
                            print('No se puede ingresar la misma contrasena\n')
                            continue
                        else:
                            password_new != password
                            password = password_new
                            print('\n'*50)
                            print('Cambio de contrasena exitoso\n')
                elif option == '2':
                    counter = 0
                    print('Usted ha elegido la opción 2\n')
                    print('Coordenadas favoritas')
                    print('-'*30)
                    print(f'coordenadas casa {home}')
                    print(f'coordenadas trabajo {work}')
                    print(f'coordenadas parque {park}\n')
                    if matriz_coordinates == []:
                        saludo()
                        home = enter_and_validation_coordinates_home()
                        work = enter_and_validation_coordinates_work()
                        park = enter_and_validation_coordinates_park()
                        is_list_empty(home, work, park)   
                        matriz_coordinates = create_matriz(home, work, park)
                    else:
                        if home < work and home < park:
                            print(f'La coordenada ubicada más al sur es casa {home}\n')
                        elif work < home and work < park:
                            print(f'La coordenada ubicada más al sur es trabajo {work}\n')
                        else:
                            print(f'La coordenada ubicada más al sur es parque {park}\n')
                            
                        matriz_coordinates = []
                        matriz_coordinates.append(home)
                        matriz_coordinates.append(work)
                        matriz_coordinates.append(park)
                        matriz_coordinates = np.array(matriz_coordinates)
                        addition_longitudes = []
                        addition_longitudes = []
                        addition_latitudes = np.sum(matriz_coordinates[:,0:1])
                        addition_longitudes = np.sum(matriz_coordinates[:,1:])
                        average_latitudes = addition_latitudes/len(matriz_coordinates)
                        average_longitudes = addition_longitudes/len(matriz_coordinates)
                        print(f'Promedio latitudes-> {average_latitudes:.3f}\nPromedio longitudes {average_longitudes:.3f}\n')
                        
                        election = input(f'1.Editar casa\n2.Editar trabajo\n3.Editar parque\n0.Volver al menu\n\n-> ')
                        if election == '1':
                            home = enter_and_validation_coordinates_home()
                            pass
                        elif election == '2':
                            work = enter_and_validation_coordinates_work()
                            pass
                        elif election == '3':
                            park = enter_and_validation_coordinates_park()
                            pass
                        elif election == '0':
                            print()
                            pass
                        else:
                            print('Error actualización')
                            sys.exit()
                    pass
                elif option == '3':
                    counter = 0 
                    print('Usted ha elegido la opción 3\n')
                    break
                elif option == '4':
                    counter = 0 
                    print('Usted ha elegido la opción 4\n')
                    break
                elif option == '5':
                    counter = 0 
                    print('Usted ha elegido la opción 5\n')  
                    break
                elif option == '6':                           # opción 6 para escoger opción preferida
                    counter = 0                # contador se reinicia a 0 por si hubo errores de ingreso 
                    print('\n'*50)
                    for n, m in enumerate(menu,1):
                        if n != 6 and n != 7:
                            print(n, m)
                    print()
                    choice = input('Seleccione opción favorita\n-> ')
                    if choice == '1':                     # el menu queda igual con la opción 1
                        print('\n'*50)
                        for n, m in enumerate(menu,1):
                            print(n, m)
                        print()
                        option = input('Elija una opción\n-> ')
                        print('\n')
                        continue
                    elif choice == '2':                   # la opción 2 queda de primera
                        resp_1 = input(guess1)
                        if resp_1 == '0':           # adivinanzas 1 y 2 para confirmar elección
                            resp_2 = input(guess2)         
                            if resp_2 == '4':
                                print('\n')          # menu actualizado
                                removed = menu.pop(1)
                                menu.insert(0, removed)
                                for n, m in enumerate(menu,1):
                                    print(n, m)
                                # for n, m in zip(numeral_menu, menu):
                                #     print(n, m)
                                # print('\n')
                                option = input('Elija una opción\n-> ')
                                print('\n')
                                continue
                            else:               # mensaje de error si ingresa dato equivocado en 2da adivinanza(vuelve a menu)
                                print('Error')
                        else:               # mensaje de error si ingresa dato equivocado en 1ra adivinanza(vuelve a menu)
                            print('Error')
                    elif choice == '3':                   # la opción 3 queda de primera
                        resp_1 = input(guess1)
                        if resp_1 == '0':           # adivinanzas 1 y 2 para confirmar elección
                            resp_2 = input(guess2)            
                            if resp_2 == '4':
                                print('\n')          # menu actualizado
                                removed = menu.pop(2)
                                menu.insert(0, removed)
                                for n, m in enumerate(menu,1):
                                    print(n, m)
                                print('\n')
                                option = input('Elija una opción\n-> ')
                                print('\n')
                                continue
                            else:               # mensaje de error si ingresa dato equivocado en 2da adivinanza(vuelve a menu)
                                print('Error')
                        else:               # mensaje de error si ingresa dato equivocado en 1ra adivinanza(vuelve a menu)
                            print('Error')
                    elif choice == '4':                   # la opción 4 queda de primera
                        resp_1 = input(guess1)
                        if resp_1 == '0':           # adivinanzas 1 y 2 para confirmar elección
                            resp_2 = input(guess2)            
                            if resp_2 == '4':
                                print('\n')          # menu actualizado
                                removed = menu.pop(3)
                                menu.insert(0, removed)
                                for n, m in enumerate(menu,1):
                                    print(n, m)
                                print('\n')
                                option = input('Elija una opción\n-> ')
                                print('\n')
                                continue
                            else:               # mensaje de error si ingresa dato equivocado en 2da adivinanza(vuelve a menu)
                                print('Error')
                        else:               # mensaje de error si ingresa dato equivocado en 1ra adivinanza(vuelve a menu)
                            print('Error')
                    elif choice == '5':                   # la opción 5 queda de primera
                        resp_1 = input(guess1)
                        if resp_1 == '0':           # adivinanzas 1 y 2 para confirmar elección
                            resp_2 = input(guess2)            
                            if resp_2 == '4':
                                print('\n')          # menu actualizado
                                removed = menu.pop(4)
                                menu.insert(0, removed)
                                for n, m in enumerate(menu,1):
                                    print(n, m)
                                print('\n')
                                option = input('Elija una opción\n-> ')
                                print('\n')
                                continue
                            else:               # mensaje de error si ingresa dato equivocado en 2da adivinanza(vuelve a menu)
                                print('Error')
                        else:               # mensaje de error si ingresa dato equivocado en 1ra adivinanza(vuelve a menu)
                            print('Error')
                    else:           # mensaje de error si ingresa un numero diferente entre 1 - 5(termina programa)
                        print('Error')
                        break
                elif option == '7':       # opción para terminar el programa
                    print('Hasta pronto')
                    good_bye()
                    break
                else:                       # mensaje de error al introducir opción en menu(4 errores seguidos termina el programa)
                    print('Error')
                    counter += 1
                    if counter == 4:
                        break
                for n, m in enumerate(menu,1):
                    print(n, m)
                print()
                option = input('Elija una opción-> \n')