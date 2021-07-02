print('\nBienvenido al sistema de ubicación para zonas públicas WIFI\n')
# usuario y contrasena predefinidos
user = '51604'
password = '40615'
print(f'Usuario {user}')
name = input('Introduzca su usuario\n-> ')  # se pide usuario predefinido
if name != user:
    print('Error')
elif name == user:
    print(f'contraseña {password}')
    clave = input('Introduzca su contraseña\n-> ')  # se pide clave predefinida
    if clave != password:
        print('Error')
    elif clave == password:
        print('CAPTCHA')
        first_num = 604
        second_num = (((6*5)-(5*4))-(4+6))
        add = first_num+second_num              
        response_captcha = int(input(f'{first_num} + {second_num} = '))  # solucionar operación matemática
        if response_captcha != add:
            print('Error')
        elif response_captcha == add:
            print('\nSesión iniciada\n ')
            print('1. Cambiar contraseña\n2. Ingresar coordenadas actuales\n3. Ubicar zona wifi más cercana\n'
                '4. Guardar archivo con ubicación cercana\n5. Actualizar registros de zonas wifi desde archivo\n'
                '6. Elegir opción de menú favorita\n7. Cerrar sesión\n')        # menu de opciones
            decision = input('Elija una opción\n-> ')
            counter = 0                # contador iniciado en 0
            while decision != '1' or decision != '2' or decision != '3' or decision != '4' or decision != '5' or decision != '6' or decision != '7':
                if decision == '1':                                 # menu de opciones escogido 1 - 7
                    print('Usted ha elegido la opción 1\n')
                    break
                elif decision == '2':
                    print('Usted ha elegido la opción 2\n')
                    break
                elif decision == '3':
                    print('Usted ha elegido la opción 3\n')
                    break
                elif decision == '4':
                    print('Usted ha elegido la opción 4\n')
                    break
                elif decision == '5':
                    print('Usted ha elegido la opción 5\n')  
                    break
                elif decision == '6':                           # opción 6 para escoger opción preferida
                    counter = 0                # contador se reinicia a 0 por si hubo errores de ingreso anteriores
                    favorite = input('\nSeleccione opción favorita\n\n1. Cambiar contraseña\n2. Ingresar coordenadas actuales\n'
                                    '3. Ubicar zona wifi más cercana\n4. Guardar archivo con ubicación cercana\n'
                                    '5. Actualizar registros de zonas wifi desde archivo\n-> ')
                    if favorite != '1' or favorite != '2' or favorite != '3' or favorite != '4' or favorite != '5':
                        if favorite == '1':                     # el menu queda igual con la opción 1
                            print('\n'*50)
                            print('1. Cambiar contraseña\n2. Ingresar coordenadas actuales\n3. Ubicar zona wifi más cercana\n'
                                '4. Guardar archivo con ubicación cercana\n5. Actualizar registros de zonas wifi desde archivo\n'
                                '6. Elegir opción de menú favorita\n7. Cerrar sesión\n')
                            decision = input('Elija una opción\n-> ')
                        elif favorite == '2':                   # la opción 2 queda de primera
                            guess1 = input('Para confirmar por favor responda:\nSe trata de un caso extraño, pues siendo'
                                        'siempre el mismo, valgo mucho o valgo nada,según el sitio en el que vaya\n-> ')
                            if guess1 == '0':           # adivinanzas 1 y 2 para confirmar elección
                                guess2 = input('Para confirmar por favor responda:\nLas estaciones del año y también los '
                                            'elementos y los puntos cardinales, ese número represento\n-> ')             
                                if guess2 == '4':
                                    print('\n'*50)          # menu actualizado
                                    print('1. Ingresar coordenadas actuales\n2. Cambiar contraseña\n3. Ubicar zona wifi más cercana\n'
                                        '4. Guardar archivo con ubicación cercana\n5. Actualizar registros de zonas wifi desde archivo\n'
                                        '6. Elegir opción de menú favorita\n7. Cerrar sesión\n')
                                    decision = input('Elija una opción\n-> ')
                                    continue
                                else:               # mensaje de error si ingresa dato equivocado en 2da adivinanza(vuelve a menu)
                                    print('Error')
                            else:               # mensaje de error si ingresa dato equivocado en 1ra adivinanza(vuelve a menu)
                                print('Error')
                        elif favorite == '3':                   # la opción 3 queda de primera
                            guess1 = input('Para confirmar por favor responda:\nSe trata de un caso extraño, pues siendo'
                                        'siempre el mismo, valgo mucho o valgo nada,según el sitio en el que vaya\n-> ')
                            if guess1 == '0':           # adivinanzas 1 y 2 para confirmar elección
                                guess2 = input('Para confirmar por favor responda:\nLas estaciones del año y también los '
                                            'elementos y los puntos cardinales, ese número represento\n-> ')
                                if guess2 == '4':
                                    print('\n'*50)          # menu actualizado
                                    print('1. Ubicar zona wifi más cercana\n2. Cambiar contraseña\n3. Ingresar coordenadas actuales\n'
                                        '4. Guardar archivo con ubicación cercana\n5. Actualizar registros de zonas wifi desde archivo\n'
                                        '6. Elegir opción de menú favorita\n7. Cerrar sesión\n')
                                    decision = input('Elija una opción\n-> ')
                                    continue
                                else:               # mensaje de error si ingresa dato equivocado en 2da adivinanza(vuelve a menu)
                                    print('Error')
                            else:               # mensaje de error si ingresa dato equivocado en 1ra adivinanza(vuelve a menu)
                                print('Error')
                        elif favorite == '4':                   # la opción 4 queda de primera
                            guess1 = input('Para confirmar por favor responda:\nSe trata de un caso extraño, pues siendo'
                                        'siempre el mismo, valgo mucho o valgo nada,según el sitio en el que vaya\n-> ')
                            if guess1 == '0':           # adivinanzas 1 y 2 para confirmar elección
                                guess2 = input('Para confirmar por favor responda:\nLas estaciones del año y también los '
                                            'elementos y los puntos cardinales, ese número represento\n-> ')
                                if guess2 == '4':
                                    print('\n'*50)          # menu actualizado
                                    print('1. Guardar archivo con ubicación cercana\n2. Cambiar contraseña\n3. Ingresar coordenadas actuales\n4. Ubicar zona wifi más cercana \n5. Actualizar registros de zonas wifi desde archivo\n'
                                        '6. Elegir opción de menú favorita\n7. Cerrar sesión\n')
                                    decision = input('Elija una opción\n-> ')
                                    continue
                                else:               # mensaje de error si ingresa dato equivocado en 2da adivinanza(vuelve a menu)
                                    print('Error')
                            else:               # mensaje de error si ingresa dato equivocado en 1ra adivinanza(vuelve a menu)
                                print('Error')
                        elif favorite == '5':                   # la opción 5 queda de primera
                            guess1 = input('Para confirmar por favor responda:\nSe trata de un caso extraño, pues siendo'
                                        'siempre el mismo, valgo mucho o valgo nada,según el sitio en el que vaya\n-> ')
                            if guess1 == '0':           # adivinanzas 1 y 2 para confirmar elección
                                guess2 = input('Para confirmar por favor responda:\nLas estaciones del año y también los '
                                            'elementos y los puntos cardinales, ese número represento\n-> ')
                                if guess2 == '4':
                                    print('\n'*50)          # menu actualizado
                                    print('1. Actualizar registros de zonas wifi desde archivo\n2. Cambiar contraseña\n3. Ingresar coordenadas actuales\n4. Ubicar zona wifi más cercana\n5. Guardar archivo con ubicación cercana\n'
                                        '6. Elegir opción de menú favorita\n7. Cerrar sesión\n')
                                    decision = input('Elija una opción\n-> ')
                                    continue
                                else:               # mensaje de error si ingresa dato equivocado en 2da adivinanza(vuelve a menu)
                                    print('Error')
                            else:               # mensaje de error si ingresa dato equivocado en 1ra adivinanza(vuelve a menu)
                                print('Error')
                        else:           # mensaje de error si ingresa un numero diferente entre 1 - 5(termina programa)
                            print('Error')
                            break
                elif decision == '7':       # opción para terminar el programa
                    print('Hasta pronto')
                    break
                else:                       # mensaje de error al introducir opción en menu(4 errores seguidos termina el programa)
                    print('Error')
                    counter += 1
                    if counter == 4:
                        break
                print('1. Cambiar contraseña\n2. Ingresar\n3. Coordenadas actuales\n3. Ubicar zona wifi más cercana\n'
                    '4. Guardar archivo con ubicación cercana\n5. Actualizar registros de zonas wifi desde archivo\n'
                    '6. Elegir opción de menú favorita\n7. Cerrar sesión\n')
                decision = input('Elija una opción-> \n')
