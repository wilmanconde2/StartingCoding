print('Calculadora')
operation = input('Digita la operación que quieres realizar (+. -. *, /,**)->')     # se pide a usuario elegir operacion a realizar
while operation != '+' or operation != '-' or operation != '*' or operation != '/' or operation != '**': # bucle operacion
    if operation == '+' or operation == '-' or operation == '*' or operation == '/' or operation == '**':
        num1 = input('Ingresa el primer numero ')   # hasta que no digite bien simbolo de operacion no pide 1er numero
        if num1.isdigit():
            num1 = float(num1)      # si digita algun caracter que no sea digito, se devuelve a escoger operacion
            num2 = input('Ingresa el segundo numero ')     # si digita bien primer numero, pide el segundo numero
            if num2.isdigit():
                num2 = float(num2)      # si digita bien segundo numero entra a realizar la operacion, si no, devuelve a escoger operacion
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