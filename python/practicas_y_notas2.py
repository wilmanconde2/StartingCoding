# SALIDAS CON FORMATO
name = 'Wilman Conde'
age = 38

print('Hola',name,'tienes',age,'años')
print('Hola {} tienes {} años'.format(name,age))
print('Hola {b} tienes {a} años'.format(a=name, b=age))
print('Hola |{a:^30}| tienes {b} años'.format(a=name, b=age))  # EL ^ para centrar elemento y los | para ver la cantidad indicada
print('Hola |{a:<30}| tienes {b} años'.format(a=name, b=age))  # < o > para mover a la izquierda o derecha
print('Hola |{a:>30}| tienes {b} años\n'.format(a=name, b=age))

print(name.upper())     # Pasa cadena a mayúsculas
print(name.lower())     # Pasa cadena a minúsculas
print(name.capitalize())    # Pone mayúscula la primera letra
print(name.swapcase())  # Las letras mayúsculas pasan a minúsculas y viceversa
print(name.center(20,'$'))  # Centra el elemento segun cantidad de espacios elegido y rellena con el caracter escogido
print(f'hola {name} tienes {age} años')
cadena = 'Hola buen dia'
print(cadena)
print(cadena.split(' '))     # Imprime una cadena como lista
print(cadena.replace('Hola', 'Chao'))    # Remplaza un elemento de la cadena
print()

# ENTRADA DE DATOS cadenas y numeros
name = input('Digite su nombre: ')
print(f'Hola {name.capitalize()}')
age = int(input('Cual es tu edad: '))
print(f'Tu edad es {age}')
number2 = float(input('Digita un numero decimal: '))
sum = age+number2
print(f'La suma de ambos números es: {sum}')
print(f'|{name:^20}| {age:^20}')       # formato para centrar cadenas :^#espacios | | sirven para saber el espacio
print(f'|{name:<20}| |{age:>20}|')        # formato para alinear a la izquierda o derecha
print(f'cadena al revés-> {name[::-1]}\n')       # imprime cadena al revés

devuelta = 2365437.87268239849
print('La variable devuelta es->', devuelta)
# Formato para elegir cuantos números mostrar despues del punto
print(f'La devuelta es {devuelta:.3f}')
# otra manera de mostrar números despues del punto
print('La devuelta es %.3f' % devuelta)
# El numero despues del % agrega espacios adelante del número
print('La devuelta es %20.5f \n' % devuelta)
