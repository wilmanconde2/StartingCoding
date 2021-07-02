# CONDICIONALES
num1 = int(input('Digita un número: '))
if num1>0:      # condición
    print(f'El número {num1} es positivo')
elif num1==0:   # condicion
    print(f'El número es 0')
else:           # si no se cumple ninguna de las anteriores, se realiza el ELSE
    print(f'El número {num1} es negativo')
print()

# CONDICIONALES ANIDADOS Y COMBINADOS
age = int(input('Digita tu edad: '))
if 0<age<100:
    print('Estas vivo!')
    if age>=18:
        print('Eres mayor de edad!!')
else:
    print('Edad incorrecta!!')