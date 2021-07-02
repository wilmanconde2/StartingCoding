'''
# 1 hipotenusa
import math
input('Calculo de hipotenusa')
cat1 = int(input('Valor primer cateto '))
cat2 = int(input('Valor segundo cateto '))
hipotenusa = math.sqrt(cat1**2+cat2**2)
input(f'El valor de la hipotenusa es {hipotenusa:.3f}')

# 2 media aritmética
input('Calculo de media aritmética de 3 números')
n1 = int(input('1er número '))
n2 = int(input('2do número '))
n3 = int(input('3er número '))
media = int((n1+n2+n3)/3)
input(f'La media aritmética de {n1}, {n2} y {n3} es= {media}')

# 3 descuento
input('Calculo de descuento')
input('Introduce el valor de tus compras')
com1 = int(input('1er compra '))
com2 = int(input('2da compra '))
com3 = int(input('3er compra '))
com4 = int(input('4ta compra '))
com5 = int(input('5ta compra '))
total = com1+com2+com3+com4+com5
input(f'Compra total ${total}')
discount = total*0.15
input(f'Tu descuento es de {discount}')
final_payment = total-discount
input(f'Total a pagar {final_payment}')

# 4 salario
input('Calculo de salario')
payment = 32000
worked_days = int(input('Ingresa número de días trabajados '))
total_salary = payment*worked_days
input(f'Tu salario sera de = $ {total_salary}')

# 5 aumento de salario 10%
input('Calculo de aumento de salario')
payment = 32000
worked_days = int(input('Ingresa número de días trabajados '))
rise = payment*worked_days*0.1
input(f'Tu aumento es de = ${rise}')
total_salary = payment*worked_days
input(f'Tu salario con aumento sera de = $ {total_salary+rise}')

# 6 celsios a farenheit
input('Calculo de Celsios a Farenheit')
grados = int(input('Ingresa los grados que quieres cambiar '))
farenheit = grados*1.8+32
input(f'{grados} Celsios son {farenheit} farenheit')

# 7 suma resta multiplicacion division
num1 = int(input('Ingresa 1er numero '))
num2 = int(input('Ingresa 2do numero '))
suma = num1+num2
resta = num1-num2
mult = num1*num2
div = num1/num2
input(f'Ingresaste los números {num1} y {num2}\nSuma {suma}\nResta {resta}\nMultiplicacion {mult}\nDivision {div}')
'''
# 8 calificación final
# TODO: terminar ejercicios