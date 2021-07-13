# ecuacion algebraica con 4 incógnitas
ecuacion = '3x+2y-7z+3w = 75'
print(f'La ecuacion es {ecuacion}')
num1 = int(input('Ingresa valor de x '))
num2 = int(input('Ingresa valor de y '))
num3 = int(input('Ingresa valor de z '))
w = (75-(3*num1)-(2*num2)+(7*num3))/3
print(f'El valor de w seria {w}')