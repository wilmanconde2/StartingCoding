print('   ____      _            _       _              ')
print('  / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __  ')
print(" | |   / _` | |/ __| | | | |/ _` | __/ _ \| '__| ")
print(" | |__| (_| | | (__| |_| | | (_| | || (_) | |    ")
print("  \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|    \n\n")                         

# se pide a usuario elegir operacion a realizar
operation = input('Digita la operación que quieres realizar (+. -. *, /,**)->')
while operation != '+' or operation != '-' or operation != '*' or operation != '/' or operation != '**':  # bucle operacion
    if operation == '+' or operation == '-' or operation == '*' or operation == '/' or operation == '**':
        # hasta que no digite bien simbolo de operacion no pide 1er numero
        num1 = input('Ingresa el primer numero ')
        if num1.isdigit():
            # si digita algun caracter que no sea digito, se devuelve a escoger operacion
            num1 = float(num1)
            # si digita bien primer numero, pide el segundo numero
            num2 = input('Ingresa el segundo numero ')
            if num2.isdigit():
                # si digita bien segundo numero entra a realizar la operacion, si no, devuelve a escoger operacion
                num2 = float(num2)
                if operation == '+':
                    add = float(num1+num2)      # operacion de suma
                    print(f'La suma de {num1} + {num2} es = {add}')
                elif operation == '-':
                    sub = float(num1-num2)      # operacion de resta
                    print(f'La resta de {num1} - {num2} es = {sub}')
                elif operation == '*':
                    mul = float(num1*num2)      # operacion de multiplicacion
                    print(f'La multiplicación de {num1} x {num2} es = {mul}')
                elif operation == '**':
                    pwr = float(num1**num2)     # operacion de potencia
                    print(f'La potencia de {num1}^{num2} es = {pwr}')
                elif operation == '/':           # operacion de division
                    if num2 == 0:               # se especifica que no se puede dividir por 0
                        print('Lo sentimos, no se puede dividir por 0')
                    else:
                        div = float(num1/num2)
                        print(f'La división de {num1} / {num2} es = {div}')
    operation = input('Digita la operación que quieres realizar (+. -. *, /,**): o "fin" para terminar el programa-> ')  # bucle operacion
    if operation == 'fin' or operation == 'FIN':      # para cerrar programa cuando el usuario decida
        break

print('     __      __.__.__                            ')
print('    /  \    /  \__|  |   _____  _____    ____    ')
print('    \   \/\/   /  |  |  /     \/\__  \  /    \   ')
print('     \        /|  |  |_|  Y Y  \/ __  \|   |  \  ')
print('      \__/\  / |__|____/__|_|  (____  / ___|  /  ')
print('           \/                \/     \/     \/    ')
print('    _________                    .___            ')
print('    \_   ___ \  ____   ____    __| _/____        ')
print('    /    \  \/ /  _ \ /    \  / __ |/ __ \       ')
print('    \     \___(  <_> )   |  \/ /_/ \  ___/       ')
print('     \______  /\____/|___|  /\____ |\___  >      ')
print('            \/            \/      \/    \/       ')