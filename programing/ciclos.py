print('     ███╗   ███╗██╗██╗  ██╗      ')
print('     ████╗ ████║██║╚██╗██╔╝      ')
print('     ██╔████╔██║██║ ╚███╔╝       ')
print('     ██║╚██╔╝██║██║ ██╔██╗       ')
print('     ██║ ╚═╝ ██║██║██╔╝ ██╗      ')
print('     ╚═╝     ╚═╝╚═╝╚═╝  ╚═╝      ')

 # se pide a usuario elegir operación a realizar 'Centinela'
menu = ['1. Saludar','2. Es par??','3. Promedio de notas','4. Residuo de division','5. Porcentaje','6. Potencia de un numero','0. Terminar programa']
for i in menu:
    print(i)
centinela = input('Elige la operación a realizar\n-> ')        # bucle del programa
while centinela != '1' or centinela != '2' or centinela != '3' or centinela != '4' or centinela != '5' or centinela != '6' or centinela != '0':  
    if centinela == '1' or centinela == '2' or centinela == '3' or centinela == '4' or centinela == '5' or centinela == '6' or centinela == '0':    

# 1 Saludar
        if centinela == '1':
            name = input('Como te llamas?\n-> ')        # pide nombre de usuario
            while True:
                try:
                    time = float(input('Que hora es (horario militar de 0 a 23.59)\n-> '))      # pide hora militar
                except ValueError:
                    print("Error, hora militar de 0 a 23.59")
                    continue
                if time >= 0 and time < 12.00:
                    print(f'Buenos días {name.capitalize()}\n')
                    break
                elif time >= 12.00 and time < 18.00:
                    print(f'Buenas tardes {name.capitalize()}\n')
                    break
                elif time >= 18.00 and time <= 23.59:
                    print(f'Buenas noches {name.capitalize()}\n')
                    break
                else:
                    print('Error de hora militar')
                
            
# 2 Es par?
        elif centinela == '2':
            num1 = input('Ingresa un número entero\n-> ')      # pide numero a evaluar
            if num1.isdigit():                      # verifica que sea un numero
                num1 = int(num1)                  # se convierte a entero si es un numero
                if num1%2 == 0:                     # operacion para saber si es par
                    print(f'EL numero {num1} es par\n')   # imprime si es par
                elif num1%2 != 0:                   # operacion para saber si es impar
                    print(f'El numero {num1} es impar\n') # imprime si es impar
            else:
                print(f'No ingresaste un número entero, lo sentimos\n')  # error al ingresar datos
                decision = input('Marca 1 para cerrar o cualquier tecla para continuar\n-> ')
                if decision == '1':
                    break
                else:
                    continue
# 3 Promedio
        elif centinela == '3':
            suma = 0                        # se declara variable por fuera del ciclo inicializada en 0 
            i = 1                           # se inicia i para control de contador en el ciclo
            num_notas = input('Ingresa la cantidad de notas a promediar\n-> ')        # se pide cantidad de notas a promediar
            if num_notas.isdigit():                 # verificacion que sea numero
                num_notas = float(num_notas)                # se convierte a flotante
                if num_notas >= 2:                  # si cumple la condicion entra al ciclo
                    num_notas = float(num_notas)            # se convierte a flotante
                    while (i <= num_notas):         # si cumple condicion entra al bucle
                        # nota = input(f'Ingresa la nota {i}\n-> ')
                        # while True:
                        try:
                            nota = float(input(f'Ingresa la nota {i}\n-> '))      # pide hora militar
                        except ValueError:
                            print("Error, digita una nota")
                            continue
                        # nota = float(nota)
                        suma = suma + nota
                        i += 1
                        promedio = suma / num_notas
                        print(f'EL promedio de notas es {promedio}\n')
                        continue
                else:
                        print('No sirve ese dato para un promedio\n')         # informa de error de datos ingresados
                        continue
            else:
                print('Ingresaste un valor equivocado\n')             # informa de error de datos ingresados
                decision = input('Marca 1 para cerrar o cualquier tecla para continuar\n-> ')
                if decision == '1':
                    break
# 4 Modulo
        elif centinela == '4':  
            num1 = input('Ingresa el dividendo\n-> ')       # se pide ingresar el numero a dividir
            if num1.isdigit():                          # TODO verificacion que sea numero (decimal)
                num1 = float(num1)                      # se convierte a flotante
                num2 = input('Ingresa el divisor\n-> ')      # TODO se pide numero divisor (decimal)
                if num2.isdigit():                      # verificacion que sea numero
                    num2 = float(num2)                  # se convierte a flotante
                    if num2 == 0:               
                        print('Lo sentimos, no se puede dividir por 0\n') # se especifica que no se puede dividir por 0
                    else:
                        mod = num1%num2                 # operacion para hallar residuo de division
                        print(f'El residuo de {num1} / {num2} es = {mod}\n')      # imprime resultado
                else:
                    print('Lo sentimos, no ingresaste correctamente los datos\n')     # error al ingresar el divisor
                    continue
            else:
                print('Lo sentimos, no ingresaste correctamente los datos\n')         # error al ingresar el dividendo
                decision = input('Marca 1 para cerrar o cualquier tecla para continuar\n-> ')
                if decision == '1':
                    break
# 5 Porcentaje
        elif centinela == '5':
            num1 = input('Escribe el número a evaluar\n-> ')   # se pide numero a evaluar
            if num1.isdigit():                   # verificacion que sea numero positivo
                num1 = float(num1)                      # se convierte a flotante
                if num1 > 0:
                    porcentage = input('Que porcentaje quieres calcular?\n-> ')     # se pide porcentaje a evaluar
                    if porcentage.isdigit():                # TODO verificacion que sea numero (decimal)
                        porcentage = float(porcentage)      # se convierte a flotante
                        result = ((num1*porcentage)/100)    # operacion para hallar porcentaje 
                        if porcentage > 0:
                            print(f'El {porcentage:.0f}% de {num1} es {result}\n')    # se imprime resultado
                        else:
                            print('Lo sentimos, no sirve ese dato como porcentaje\n')   # error al ingresar porcentaje
                            continue
                    else:
                        print('Lo sentimos, no sirve ese dato como porcentaje\n')
                        continue
                else:
                    print('Lo sentimos, no sirve ese dato como porcentaje\n')
            else:
                print('Lo sentimos, intenta de nuevo\n')       # error al ingresar numero a evaluar
                decision = input('Marca 1 para cerrar o cualquier tecla para continuar\n-> ')
                if decision == '1':
                    break
# 6 Potencia
        elif centinela == '6':
            num1 = input('Ingresa el número base\n-> ')     # se pide numero base a evaluar
            if num1.isdigit():                          # TODO verificacion que sea numero (decimal)
                num1 = float(num1)                      # se convierte a flotante
                pwr = None                              # declaración de variable vacia 
                digits = ('2', '3', '4', '5', '6', '7', '8', '9','10')      # lista de numeros a recorrer como potencias
                for pwr in digits:                      # bucle para recorrer lista
                    pwr = float(pwr)                    # se convierte a flotante
                    result = float(num1**pwr)           # variable declarada para resultado de potencia
                    print(f'El numero {num1:.0f} elevado a {pwr:.0f} es {result:.0f}\n')    # se imprime resultados
            else:
                print('Lo sentimos, no ingresaste bien los datos\n')   # error al ingresar numero base
                decision = input('Marca 1 para cerrar o cualquier tecla para continuar\n-> ')
                if decision == '1':
                    break
                else:
                    continue
# 0 Salir
        elif centinela == '0':                # para cerrar el programa 
               
            print('     ██╗    ██╗ ██████╗██████╗       ')
            print('     ██║    ██║██╔════╝╚════██╗      ')
            print('     ██║ █╗ ██║██║      █████╔╝      ')
            print('     ██║███╗██║██║     ██╔═══╝       ')
            print('     ╚███╔███╔╝╚██████╗███████╗      ')
            print('      ╚══╝╚══╝  ╚═════╝╚══════╝      ')
            print('Programa finalizado \n')
            break
    for i in menu:
        print(i)
    centinela = input('Elige la operación a realizar\n-> ') 