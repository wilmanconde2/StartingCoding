import sys                                                                     
import math as mt
import numpy as np

def saludo_inicial():
        
    print('''
    ________   __            __    __             __             ______                                 
    |        \|  \          |  \  |  \           |  \           /      \                                
    \$$$$$$$$ \ $$  _______ | $$\ | $$  ______  _| $$_         |  $$$$$$\  ______    ______    ______   
        | $$   |  \ /       \| $$$\| $$ /      \|   $$ \        | $$   \$$ /      \  /      \  /      \  
        | $$   | $$|  $$$$$$$| $$$$\ $$|  $$$$$$\ \$$$$$$       | $$      |  $$$$$$\|  $$$$$$\|  $$$$$$\ 
        | $$   | $$| $$      | $$\$$ $$| $$    $$ | $$ __       | $$   __ | $$  | $$| $$   \$$| $$  | $$ 
        | $$   | $$| $$_____ | $$ \$$$$| $$$$$$$$ | $$|  \      | $$__/  \| $$__/ $$| $$      | $$__/ $$ 
        | $$   | $$ \$$     \| $$  \$$$ \$$     \  \$$  $$       \$$    $$ \$$    $$| $$      | $$    $$ 
        \ $$    \$$  \$$$$$$$ \$$   \$$  \$$$$$$$   \$$$$         \$$$$$$   \$$$$$$  \$$      | $$$$$$$  
                                                                                            | $$       
                                                                                            | $$       
                                                                                            \$$          
    \nBienvenido al sistema de ubicación para zonas públicas WIFI\n     ''')
    return

def ingresar_coordenadas():
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
    if len(home) == 0 or len(work) == 0 or len(park) == 0:
        print('Error')
        sys.exit()
        
def create_matriz(home, work, park):
    matriz_coordinates = []
    matriz_coordinates.append(home)
    matriz_coordinates.append(work)
    matriz_coordinates.append(park)
    matriz_coordinates = np.array(matriz_coordinates)
    return matriz_coordinates
    
def calculate_wifi_distance(point1, point2):
    r_tierra = 6372.795477598
    coor2 = point2
    point1 = mt.radians(point1[0]), mt.radians(point1[1])
    point2 = mt.radians(point2[0]), mt.radians(point2[1])
        
    lat1 = point1[0]
    lat2 = point2[0]
    lon1 = point1[1]
    lon2 = point2[1]
    dlat = (lat2 - lat1)
    dlon = (lon2 - lon1)
    a = ((mt.sin(dlat/2)**2) + mt.cos(lat1) * mt.cos(lat2) * mt.sin(dlon/2)**2)
    c = 2 * r_tierra * mt.asin(mt.sqrt(a))
    distancia = c * 1000
    return distancia, coor2

def good_bye():
    print('''
       ___     ___     ___     ___     ___     ___     ___   
      / __|   | _ \   /   \   / __|   |_ _|   /   \   / __|  
     | (_ |   |   /   | - |  | (__     | |    | - |   \__ \  
      \___|   |_|_\   |_|_|   \___|   |___|   |_|_|   |___/  
    _|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
    "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
    ''')
    
user = '51604'
password = '40615'
home, work, park, matriz_coordinates = [], [], [], []
election = ''
menu = ['Cambiar contraseña','Ingresar coordenadas actuales','Ubicar zona wifi más cercana',
        'Guardar archivo con ubicación cercana','Actualizar registros de zonas wifi desde archivo',
        'Elegir opción de menú favorita','Cerrar sesión']
guess1 = ('Para confirmar por favor responda:\nSe trata de un caso extraño, pues siendo'
          'siempre el mismo, valgo mucho o valgo nada,según el sitio en el que vaya\n-> ')
guess2 = ('Para confirmar por favor responda:\nLas estaciones del año y también los '
          'elementos y los puntos cardinales, ese número represento\n-> ') 
wifi_zones = [[-3.777, -70.302, 91],[-4.134, -69.983, 233],[-4.006, -70.132, 149],[-3.846, -70.222, 211]]
wifi_zones = np.array(wifi_zones)
wifi_predet = [[-3.002, -69.714],[-4.227,-70.365]]

# Inicio del programa
saludo_inicial()
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
            print(50 * '\n')
            print('-' * 150)
            print('\nSesión iniciada\n ')
            for n, m in enumerate(menu,1):
                print(n, m)
            print()
            option = input('Elija una opción\n-> ')
            print(50 * '\n')
            print('-' * 150)
            counter = 0                # contador iniciado en 0
            while True:
                if option == '1':                                 # menu de opciones escogido 1 - 7
                    print(50 * '\n')
                    print('-' * 150)
                    counter = 0                     # contador se reinicia a 0 
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
                            print(50 * '\n')
                            print('-' * 150)
                            print('Cambio de contrasena exitoso\n')
                elif option == '2':
                    print(50 * '\n')
                    print('-' * 150)
                    counter = 0                     # contador se reinicia a 0
                    print('Usted ha elegido la opción 2\n')
                    print('Coordenadas favoritas')
                    print('-'*30)
                    print(f'Coordenadas casa {home}\nCoordenadas trabajo {work}\nCoordenadas parque {park}\n')
                    
                    if len(matriz_coordinates) < 2:
                        ingresar_coordenadas()
                        home = enter_and_validation_coordinates_home()
                        work = enter_and_validation_coordinates_work()
                        park = enter_and_validation_coordinates_park()
                        is_list_empty(home, work, park)   
                        matriz_coordinates = create_matriz(home, work, park)
                        print(50 * '\n')
                        print('-' * 150)
                    else:
                        if home < work and home < park:
                            print(f'La coordenada ubicada más al sur es casa {home}\n')
                        elif work < home and work < park:
                            print(f'La coordenada ubicada más al sur es trabajo {work}\n')
                        else:
                            print(f'La coordenada ubicada más al sur es parque {park}\n')
                            
                        create_matriz(home, work, park)
                        addition_latitudes = []
                        addition_longitudes = []
                        addition_latitudes = np.sum(matriz_coordinates[:,0:1])
                        addition_longitudes = np.sum(matriz_coordinates[:,1:])
                        average_latitudes = addition_latitudes/len(matriz_coordinates)
                        average_longitudes = addition_longitudes/len(matriz_coordinates)
                        print(f'Promedio latitudes-> {average_latitudes:.3f}\nPromedio longitudes {average_longitudes:.3f}\n')
                        
                        election = input(f'1.Editar casa\n2.Editar trabajo\n3.Editar parque\n0.Volver al menu\n-> ')
                        if election == '1':
                            home = enter_and_validation_coordinates_home()
                            print(50 * '\n')
                            print('-' * 150)
                            pass
                        elif election == '2':
                            work = enter_and_validation_coordinates_work()
                            print(50 * '\n')
                            print('-' * 150)
                            pass
                        elif election == '3':
                            park = enter_and_validation_coordinates_park()
                            print(50 * '\n')
                            print('-' * 150)
                            pass
                        elif election == '0':
                            print(50 * '\n')
                            print('-' * 150)            
                            pass
                        else:
                            print('Error actualización')
                            sys.exit()
                    pass
                
                elif option == '3':
                    print(50 * '\n')
                    print('-' * 150)
                    counter = 0                     # contador se reinicia a 0 
                    print('Usted ha elegido la opción 3\n')
                    if len(matriz_coordinates) < 2:
                        print('Error sin registro de coordenadas')
                        sys.exit()
                    else:
                        print(f'Coordenada [latitud,longitud] 1: {home}\nCoordenada [latitud,longitud] 2: {work}\nCoordenada [latitud,longitud] 3. {park}\n')  
                        matriz_coordinates = list(matriz_coordinates)
                        election = input('Por favor elija su ubicación actual (1, 2 ó 3) para calcular la distancia'
                                         ' a los puntos de conexión\n-> ')
                        if election == '1':
                            print(50 * '\n')
                            print('-' * 150)
                            print()
                            # Verificacion de las coordenadas de los puntos cercanos
                            for coordinates in wifi_zones:
                                latitude = coordinates[0]
                                longitude = coordinates[1]
                                if not -4.227 <= latitude <= -3.002:
                                    print("Error coordenada")
                                    sys.exit()
                                if not -70.365 <= longitude <= -69.714:
                                    print("Error coordenada")
                                    sys.exit()
                            
                            calculate_distance1 = calculate_wifi_distance(home, wifi_zones[0])
                            calculate_distance2 = calculate_wifi_distance(home, wifi_zones[1])
                            calculate_distance3 = calculate_wifi_distance(home, wifi_zones[2])
                            calculate_distance4 = calculate_wifi_distance(home, wifi_zones[3])
                            close_wifi = [calculate_distance1, calculate_distance2, calculate_distance3, calculate_distance4]
                            close_wifi.sort()
                            position1home = close_wifi[0]
                            users_spot1 = int(position1home[-1][2])
                            distance1 = int(position1home[0])
                            latitude1 = float(position1home[-1][0])
                            longitude1 = float(position1home[-1][1])
                            position2home = close_wifi[1]
                            users_spot2 = int(position2home[-1][2])
                            distance2 = int(position2home[0])
                            latitude2 = float(position2home[-1][0])
                            longitude2 = float(position2home[-1][1])
                            lathome = float(home[0])
                            lonhome = float(home[1])
                            
                            if users_spot1 < users_spot2:
                                print('La zona wifi 1: ubicada en' , position1home[-1][0:2] , ' a ' , distance1 , ' metros, tiene en promedio ' , users_spot1 , ' usuarios\nLa zona wifi 2: ubicada en ' , position2home[-1][0:2] , ' a ' , distance2 , ' metros, tiene en promedio ' , users_spot2 , ' usuarios')
                            elif users_spot1 > users_spot2:
                                print('La zona wifi 1: ubicada en' , position2home[-1][0:2] ,' a ' , distance2 , ' metros, tiene en promedio ' , users_spot2 , ' usuarios\nLa zona wifi 2: ubicada en ' , position1home[-1][0:2] , ' a ' , distance1 , ' metros, tiene en promedio ' , users_spot1 , ' usuarios')
                                                                   
                            choice_direction = input('Elija 1 o 2 para recibir indicaciones de llegada\n-> ')
                            if choice_direction == '1':                                
                                if lathome >= latitude1:
                                    go_to_latitude = 'sur'
                                elif lathome <= latitude1:
                                    go_to_latitude = 'norte'
                                if lonhome >= longitude1:
                                    go_to_longitude = 'occidente'
                                elif lonhome <= longitude1:
                                    go_to_longitude = 'oriente'
                                print()
                                if users_spot1 < users_spot2:
                                    print(f'Para llegar a la zona wifi dirigirse primero al {go_to_longitude} y luego hacia el {go_to_latitude}\nEl tiempo promedio en moto es de {int((distance1/19.44)/60)} minutos\nEL tiempo promedio en bicicleta es de {int((distance1/3.33)/60)} minutos')
                                else:
                                    print(f'Para llegar a la zona wifi dirigirse primero al {go_to_longitude} y luego hacia el {go_to_latitude}\nEl tiempo promedio en moto es de {int((distance2/19.44)/60)} minutos\nEL tiempo promedio en bicicleta es de {int((distance2/3.33)/60)} minutos')
                                print('\n')
                            
                            elif choice_direction == '2':
                                if lathome >= latitude2:
                                    go_to_latitude = 'sur'
                                elif lathome <= latitude2:
                                    go_to_latitude = 'norte'
                                if lonhome >= longitude2:
                                    go_to_longitude = 'occidente'
                                elif lonhome <= longitude2:
                                    go_to_longitude = 'oriente'
                                print()
                                if users_spot2 > users_spot1:
                                    print(f'Para llegar a la zona wifi dirigirse primero al {go_to_longitude} y luego hacia el {go_to_latitude}\nEl tiempo promedio en moto es de {int((distance2/19.44)/60)} minutos\nEL tiempo promedio en bicicleta es de {int((distance2/3.33)/60)} minutos')
                                else:
                                    print(f'Para llegar a la zona wifi dirigirse primero al {go_to_longitude} y luego hacia el {go_to_latitude}\nEl tiempo promedio en moto es de {int((distance1/19.44)/60)} minutos\nEL tiempo promedio en bicicleta es de {int((distance1/3.33)/60)} minutos')
                                print('\n')
                                
                            else:
                                print('Error zona wifi')
                                sys.exit()
                                
                        elif election == '2':
                            print(50 * '\n')
                            print('-' * 150)
                            print()
                            # Verificación de las coordenadas de los puntos cercanos
                            for coordinates in wifi_zones:
                                latitude = coordinates[0]
                                longitude = coordinates[1]
                                if not -4.227 <= latitude <= -3.002:
                                    print("Error coordenada")
                                    sys.exit()
                                if not longitude >= -70.365 and longitude <= -69.714:
                                    print("Error coordenada")
                                    sys.exit()
                            
                            calculate_distance1 = calculate_wifi_distance(work, wifi_zones[0])
                            calculate_distance2 = calculate_wifi_distance(work, wifi_zones[1])
                            calculate_distance3 = calculate_wifi_distance(work, wifi_zones[2])
                            calculate_distance4 = calculate_wifi_distance(work, wifi_zones[3])
                            close_wifi = [calculate_distance1, calculate_distance2, calculate_distance3, calculate_distance4]
                            close_wifi.sort()
                            position1work = close_wifi[0]
                            users_spot1 = int(position1work[-1][2])
                            distance1 = int(position1work[0])
                            latitude1 = float(position1work[-1][0])
                            longitude1 = float(position1work[-1][1])
                            position2work = close_wifi[1]
                            users_spot2 = int(position2work[-1][2])
                            distance2 = int(position2work[0])
                            latitude2 = float(position2work[-1][0])
                            longitude2 = float(position2work[-1][1])
                            latwork = float(work[0])
                            lonwork = float(work[1])
                            
                            if users_spot1 < users_spot2:
                                print('La zona wifi 1: ubicada en' , position1work[-1][0:2] , ' a ' , distance1 , ' metros, tiene en promedio ' , users_spot1 , ' usuarios\nLa zona wifi 2: ubicada en ' , position2work[-1][0:2] , ' a ' , distance2 , ' metros, tiene en promedio ' , users_spot2 , ' usuarios')
                            elif users_spot1 > users_spot2:
                                print('La zona wifi 1: ubicada en' , position2work[-1][0:2] ,' a ' , distance2 , ' metros, tiene en promedio ' , users_spot2 , ' usuarios\nLa zona wifi 2: ubicada en ' , position1work[-1][0:2] , ' a ' , distance1 , ' metros, tiene en promedio ' , users_spot1 , ' usuarios')
                                                                   
                            choice_direction = input('Elija 1 o 2 para recibir indicaciones de llegada\n-> ')
                            if choice_direction == '1':                                
                                if latwork >= latitude1:
                                    go_to_latitude = 'sur'
                                elif latwork <= latitude1:
                                    go_to_latitude = 'norte'
                                if lonwork >= longitude1:
                                    go_to_longitude = 'occidente'
                                elif lonwork <= longitude1:
                                    go_to_longitude = 'oriente'
                                print()
                                if users_spot1 < users_spot2:
                                    print(f'Para llegar a la zona wifi dirigirse primero al {go_to_longitude} y luego hacia el {go_to_latitude}\nEl tiempo promedio en moto es de {int((distance1/19.44)/60)} minutos\nEL tiempo promedio en bicicleta es de {int((distance1/3.33)/60)} minutos')
                                else:
                                    print(f'Para llegar a la zona wifi dirigirse primero al {go_to_longitude} y luego hacia el {go_to_latitude}\nEl tiempo promedio en moto es de {int((distance2/19.44)/60)} minutos\nEL tiempo promedio en bicicleta es de {int((distance2/3.33)/60)} minutos')
                                print('\n')
                            
                            elif choice_direction == '2':
                                if latwork >= latitude2:
                                    go_to_latitude = 'sur'
                                elif latwork <= latitude2:
                                    go_to_latitude = 'norte'
                                if lonwork >= longitude2:
                                    go_to_longitude = 'occidente'
                                elif lonwork <= longitude2:
                                    go_to_longitude = 'oriente'
                                print()
                                if users_spot2 > users_spot1:
                                    print(f'Para llegar a la zona wifi dirigirse primero al {go_to_longitude} y luego hacia el {go_to_latitude}\nEl tiempo promedio en moto es de {int((distance2/19.44)/60)} minutos\nEL tiempo promedio en bicicleta es de {int((distance2/3.33)/60)} minutos')
                                else:
                                    print(f'Para llegar a la zona wifi dirigirse primero al {go_to_longitude} y luego hacia el {go_to_latitude}\nEl tiempo promedio en moto es de {int((distance1/19.44)/60)} minutos\nEL tiempo promedio en bicicleta es de {int((distance1/3.33)/60)} minutos')
                                print('\n')
                                
                            else:
                                print('Error zona wifi')
                                sys.exit()
                            
                        elif election == '3':
                            print(50 * '\n')
                            print('-' * 150)
                            print()
                            # Verificación de las coordenadas de los puntos cercanos
                            for coordinates in wifi_zones:
                                latitude = coordinates[0]
                                longitude = coordinates[1]
                                if not -4.227 <= latitude <= -3.002:
                                    print("Error coordenada")
                                    sys.exit()
                                if not longitude >= -70.365 and longitude <= -69.714:
                                    print("Error coordenada")
                                    sys.exit()
                            
                            calculate_distance1 = calculate_wifi_distance(park, wifi_zones[0])
                            calculate_distance2 = calculate_wifi_distance(park, wifi_zones[1])
                            calculate_distance3 = calculate_wifi_distance(park, wifi_zones[2])
                            calculate_distance4 = calculate_wifi_distance(park, wifi_zones[3])
                            close_wifi = [calculate_distance1, calculate_distance2, calculate_distance3, calculate_distance4]
                            close_wifi.sort()                            
                            position1park = close_wifi[0]
                            users_spot1 = int(position1park[-1][2])
                            distance1 = int(position1park[0])
                            latitude1 = float(position1park[-1][0])
                            longitude1 = float(position1park[-1][1])
                            position2park = close_wifi[1]
                            users_spot2 = int(position2park[-1][2])
                            distance2 = int(position2park[0])
                            latitude2 = float(position2park[-1][0])
                            longitude2 = float(position2park[-1][1])
                            latpark = float(park[0])
                            lonpark = float(park[1])
                            
                            if users_spot1 < users_spot2:
                                print('La zona wifi 1: ubicada en' , position1park[-1][0:2] , ' a ' , distance1 , ' metros, tiene en promedio ' , users_spot1 , ' usuarios\nLa zona wifi 2: ubicada en ' , position2park[-1][0:2] , ' a ' , distance2 , ' metros, tiene en promedio ' , users_spot2 , ' usuarios')
                            elif users_spot1 > users_spot2:
                                print('La zona wifi 1: ubicada en' , position2park[-1][0:2] ,' a ' , distance2 , ' metros, tiene en promedio ' , users_spot2 , ' usuarios\nLa zona wifi 2: ubicada en ' , position1park[-1][0:2] , ' a ' , distance1 , ' metros, tiene en promedio ' , users_spot1 , ' usuarios')
                                                                   
                            choice_direction = input('Elija 1 o 2 para recibir indicaciones de llegada\n-> ')
                            if choice_direction == '1':                                
                                if latpark >= latitude1:
                                    go_to_latitude = 'sur'
                                elif latpark <= latitude1:
                                    go_to_latitude = 'norte'
                                if lonpark >= longitude1:
                                    go_to_longitude = 'occidente'
                                elif lonpark <= longitude1:
                                    go_to_longitude = 'oriente'
                                print()
                                if users_spot1 < users_spot2:
                                    print(f'Para llegar a la zona wifi dirigirse primero al {go_to_longitude} y luego hacia el {go_to_latitude}\nEl tiempo promedio en moto es de {int((distance1/19.44)/60)} minutos\nEL tiempo promedio en bicicleta es de {int((distance1/3.33)/60)} minutos')
                                else:
                                    print(f'Para llegar a la zona wifi dirigirse primero al {go_to_longitude} y luego hacia el {go_to_latitude}\nEl tiempo promedio en moto es de {int((distance2/19.44)/60)} minutos\nEL tiempo promedio en bicicleta es de {int((distance2/3.33)/60)} minutos')
                                print('\n')
                            
                            elif choice_direction == '2':
                                if latpark >= latitude2:
                                    go_to_latitude = 'sur'
                                elif latpark <= latitude2:
                                    go_to_latitude = 'norte'
                                if lonpark >= longitude2:
                                    go_to_longitude = 'occidente'
                                elif lonpark <= longitude2:
                                    go_to_longitude = 'oriente'
                                print()
                                if users_spot2 > users_spot1:
                                    print(f'Para llegar a la zona wifi dirigirse primero al {go_to_longitude} y luego hacia el {go_to_latitude}\nEl tiempo promedio en moto es de {int((distance2/19.44)/60)} minutos\nEL tiempo promedio en bicicleta es de {int((distance2/3.33)/60)} minutos')
                                else:
                                    print(f'Para llegar a la zona wifi dirigirse primero al {go_to_longitude} y luego hacia el {go_to_latitude}\nEl tiempo promedio en moto es de {int((distance1/19.44)/60)} minutos\nEL tiempo promedio en bicicleta es de {int((distance1/3.33)/60)} minutos')
                                print('\n')
                                
                            else:
                                print('Error zona wifi')
                                sys.exit()
                        else: 
                            print('Error ubicación')
                            sys.exit()
                
                elif option == '4':
                    print(50 * '\n')
                    print('-' * 150)
                    counter = 0                     # contador se reinicia a 0 
                    print('Usted ha elegido la opción 4\n')
                    
                    if len(matriz_coordinates) < 2 or choice_direction == '':
                            print(50 * '\n')
                            print('-' * 150)
                            print('Error de alistamiento')
                            sys.exit()
                    else:
                        information = {}
                        if election == '1':
                            if users_spot1 < users_spot2:
                                zonewifi = position1home[-1][0:]
                                information['actual'] = home
                                information['zonawifi1'] = zonewifi
                                information['recorrido'] = [(f'{distance1} metros'), ('bus / bicicleta'), ((f'{int((distance1/19.44)/60)} minutos'), (f'{int((distance1/3.33)/60)} minutos'))]
                                for i in information:
                                    print(i, information[i])
                                export = input('\n¿Está de acuerdo con la información a exportar? Presione 1 para confirmar,'
                                      '0 para regresar al menú principal\n->')
                                if export == '0':
                                    print(50 * '\n')
                                    print('-' * 150)
                                    pass
                                elif export == '1':
                                    print(50 * '\n')
                                    print('-' * 150)
                                    print('Exportando archivo')
                                    sys.exit()                                      
                                    
                            elif users_spot1 > users_spot2:
                                zonewifi = position2home[-1][0:]
                                information['actual'] = home
                                information['zonawifi1'] = zonewifi
                                information['recorrido'] = [(f'{distance2} metros'), ('bus / bicicleta'), ((f'{int((distance2/19.44)/60)} minutos'), (f'{int((distance2/3.33)/60)} minutos'))]
                                for i in information:
                                    print(i, information[i])
                                export = input('\n¿Está de acuerdo con la información a exportar? Presione 1 para confirmar,'
                                      '0 para regresar al menú principal\n->')
                                if export == '0':
                                    print(50 * '\n')
                                    print('-' * 150)
                                    pass
                                elif export == '1':
                                    print(50 * '\n')
                                    print('-' * 150)
                                    print('Exportando archivo')
                                    sys.exit()                                                           
                        
                        elif election == '2':
                            if users_spot1 < users_spot2:
                                zonewifi = position1work[-1][0:]
                                information['actual'] = work
                                information['zonawifi1'] = zonewifi
                                information['recorrido'] = [(f'{distance1} metros'), ('bus / bicicleta'), ((f'{int((distance1/19.44)/60)} minutos'), (f'{int((distance1/3.33)/60)} minutos'))]
                                for i in information:
                                    print(i, information[i])
                                export = input('\n¿Está de acuerdo con la información a exportar? Presione 1 para confirmar,'
                                      '0 para regresar al menú principal\n->')
                                if export == '0':
                                    print(50 * '\n')
                                    print('-' * 150)
                                    pass
                                elif export == '1':
                                    print(50 * '\n')
                                    print('-' * 150)
                                    print('Exportando archivo')
                                    sys.exit()                                    
                                                                        
                            elif users_spot1 > users_spot2:
                                zonewifi = position2work[-1][0:]
                                information['actual'] = work
                                information['zonawifi1'] = zonewifi
                                information['recorrido'] = [(f'{distance2} metros'), ('bus / bicicleta'), ((f'{int((distance2/19.44)/60)} minutos'), (f'{int((distance2/3.33)/60)} minutos'))]
                                for i in information:
                                    print(i, information[i])
                                export = input('\n¿Está de acuerdo con la información a exportar? Presione 1 para confirmar,'
                                      '0 para regresar al menú principal\n->')
                                if export == '0':
                                    print(50 * '\n')
                                    print('-' * 150)
                                    pass
                                elif export == '1':
                                    print(50 * '\n')
                                    print('-' * 150)
                                    print('Exportando archivo')
                                    sys.exit()                                    
                                                    
                        if election == '3':
                            if users_spot1 < users_spot2:
                                zonewifi = position1park[-1][0:]
                                information['actual'] = park
                                information['zonawifi1'] = zonewifi
                                information['recorrido'] = [(f'{distance1} metros'), ('bus / bicicleta'), ((f'{int((distance1/19.44)/60)} minutos'), (f'{int((distance1/3.33)/60)} minutos'))]
                                for i in information:
                                    print(i, information[i])
                                export = input('\n¿Está de acuerdo con la información a exportar? Presione 1 para confirmar,'
                                      '0 para regresar al menú principal\n->')
                                if export == '0':
                                    print(50 * '\n')
                                    print('-' * 150)
                                    pass
                                elif export == '1':
                                    print(50 * '\n')
                                    print('-' * 150)
                                    print('Exportando archivo')
                                    sys.exit()                                     
                                                                       
                            elif users_spot1 > users_spot2:
                                zonewifi = position2park[-1][0:]
                                information['actual'] = park
                                information['zonawifi1'] = zonewifi
                                information['recorrido'] = [(f'{distance2} metros'), ('bus / bicicleta'), ((f'{int((distance2/19.44)/60)} minutos'), (f'{int((distance2/3.33)/60)} minutos'))]
                                for i in information:
                                    print(i, information[i])
                                export = input('\n¿Está de acuerdo con la información a exportar? Presione 1 para confirmar,'
                                      '0 para regresar al menú principal\n->')
                                if export == '0':
                                    print(50 * '\n')
                                    print('-' * 150)
                                    pass
                                elif export == '1':
                                    print(50 * '\n')
                                    print('-' * 150)
                                    print('Exportando archivo')
                                    sys.exit()                                           
                                                                       
                elif option == '5':
                    print(50 * '\n')
                    print('-' * 150)
                    counter = 0                     # contador se reinicia a 0 
                    print('Usted ha elegido la opción 5\n')  
                    
                    # archivo = open(r'C:\Users\WC2\Desktop\UPB\upb\programing\reto5datos.csv')
                    # print(archivo.read())
                    decition = input('Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal\n-> ')
                    if decition == '0':
                        print(50 * '\n')
                        print('-' * 150)
                        pass
                    else:
                        sys.exit()
                
                elif option == '6':                           # opción 6 para escoger opción preferida
                    print(50 * '\n')
                    print('-' * 150)
                    counter = 0                     # contador se reinicia a 0       
                    print(50 * '\n')
                    print('-' * 150)
                    for n, m in enumerate(menu,1):
                        if n != 6 and n != 7:
                            print(n, m)
                    print()
                    choice_favorite = input('Seleccione opción favorita\n-> ')
                    if choice_favorite == '1':                     # el menu queda igual con la opción 1
                        print(50 * '\n')
                        print('-' * 150)
                        for n, m in enumerate(menu,1):
                            print(n, m)
                        print()
                        option = input('Elija una opción\n-> ')
                        print('\n')
                        continue
                    elif choice_favorite == '2':                   # la opción 2 queda de primera
                        resp_1 = input(guess1)
                        if resp_1 == '0':           # adivinanzas 1 y 2 para confirmar elección
                            resp_2 = input(guess2)         
                            if resp_2 == '4':
                                print(50 * '\n')
                                print('-' * 150)          
                                removed = menu.pop(1)
                                menu.insert(0, removed)
                                for n, m in enumerate(menu,1):
                                    print(n, m)                 # menu actualizado
                                option = input('Elija una opción\n-> ')
                                print('\n')
                                continue
                            else:               # mensaje de error si ingresa dato equivocado en 2da adivinanza(vuelve a menu)
                                print('Error')
                        else:               # mensaje de error si ingresa dato equivocado en 1ra adivinanza(vuelve a menu)
                            print('Error')
                    elif choice_favorite == '3':                   # la opción 3 queda de primera
                        resp_1 = input(guess1)
                        if resp_1 == '0':           # adivinanzas 1 y 2 para confirmar elección
                            resp_2 = input(guess2)            
                            if resp_2 == '4':
                                print(50 * '\n')
                                print('-' * 150)                    
                                removed = menu.pop(2)
                                menu.insert(0, removed)
                                for n, m in enumerate(menu,1):
                                    print(n, m)                     # menu actualizado
                                print('\n')
                                option = input('Elija una opción\n-> ')
                                print('\n')
                                continue
                            else:               # mensaje de error si ingresa dato equivocado en 2da adivinanza(vuelve a menu)
                                print('Error')
                        else:               # mensaje de error si ingresa dato equivocado en 1ra adivinanza(vuelve a menu)
                            print('Error')
                    elif choice_favorite == '4':                   # la opción 4 queda de primera
                        resp_1 = input(guess1)
                        if resp_1 == '0':           # adivinanzas 1 y 2 para confirmar elección
                            resp_2 = input(guess2)            
                            if resp_2 == '4':
                                print(50 * '\n')
                                print('-' * 150)          
                                removed = menu.pop(3)
                                menu.insert(0, removed)
                                for n, m in enumerate(menu,1):
                                    print(n, m)                     # menu actualizado
                                print('\n')
                                option = input('Elija una opción\n-> ')
                                print('\n')
                                continue
                            else:               # mensaje de error si ingresa dato equivocado en 2da adivinanza(vuelve a menu)
                                print('Error')
                        else:               # mensaje de error si ingresa dato equivocado en 1ra adivinanza(vuelve a menu)
                            print('Error')
                    elif choice_favorite == '5':                   # la opción 5 queda de primera
                        resp_1 = input(guess1)
                        if resp_1 == '0':           # adivinanzas 1 y 2 para confirmar elección
                            resp_2 = input(guess2)            
                            if resp_2 == '4':
                                print(50 * '\n')
                                print('-' * 150)          
                                removed = menu.pop(4)
                                menu.insert(0, removed)
                                for n, m in enumerate(menu,1):
                                    print(n, m)                     # menu actualizado
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
                        sys.exit()
                elif option == '7':       # opción para terminar el programa
                    print(50 * '\n')
                    print('-' * 150)
                    good_bye()
                    print('Hasta pronto')
                    sys.exit()
                else:                       # mensaje de error al introducir opción en menu(4 errores seguidos termina el programa)
                    print('Error')
                    counter += 1
                    if counter == 4:
                        print(50 * '\n')
                        print('-' * 150)
                        sys.exit()
                for n, m in enumerate(menu,1):
                    print(n, m)
                print()
                option = input('Elija una opción-> \n')