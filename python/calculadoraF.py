import sys

def suma(a, b):
    resultado = a + b
    return resultado
def resta(a, b):
    resultado = a - b
    return resultado
def multiplicacion(a, b):
    resultado = a * b
    return resultado
def division(a, b):
    if b != 0:
        resultado = a / b
        return resultado
    return 'No se puede dividir por 0'
def numeros():
    try:
        num1 = float(input('Numero 1\n-> '))
        num2 = float(input('Numero 2\n-> '))
    except:
        print('Valor no valido')
        print('-' * 50)
        inicio()
    return num1, num2
def inicio():
    print('Calculadora')
    operacion = input('Operacion a realizar\n0. salir\n1. +\n2. -\n3. *\n4. /\n-> ')
    if operacion == '0':
        sys.exit()
    if operacion == '1':
        num1,num2 = numeros()
        res = suma(num1, num2)
        print(res)
    if operacion == '2':
        num1,num2 = numeros()
        res = resta(num1,num2)
        print(res)
    if operacion == '3':
        num1,num2 = numeros()
        res = multiplicacion(num1,num2)
        print(res)
    if operacion == '4':
        num1,num2 = numeros()
        res = division(num1,num2)
        print(res)
    print('-' * 50)
    inicio()

inicio()