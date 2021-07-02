# CALCULADORA 2BARFI
# Calculadora cachorros
import math
def puppies_calculator (a,b):
    if a >= 0 and a < 2:
        print('Comunicate con nosotros para brindarte toda la información')
    elif a >= 2 and a < 4:
        print(0.1 * b)
    elif a >= 4 and a < 6:
        print(0.08 * b)
    elif a >= 6 and a < 8:
        print(0.06 * b)
    elif a >= 8 and a < 10:
        print(0.04 * b)
    elif a >= 10 and a < 12:
        print(0.03 * b)
    else:
        print('Datos incorrectos')

print('Calculadora para cachorros de 2 a 12 meses!')
print()
edad = int(input('ingresar edad en meses (2 a 12): '))
peso = int(input('ingresar peso actual en gramos (1 kl y medio = 1500 gms):  '))

puppies_calculator(edad,peso)
print('Gramos aproximadamente')