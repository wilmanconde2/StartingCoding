# FUNCIONES

# suma
def add(a,b):
    z = (a + b)
    return z     # Con return la funcion devuelve un resultado
result1 = add(2, 6)
print(result1)

# resta
def substraction():
    x = input('Ingrese x ')
    y = input('Ingrese y ')       # Pedimos numeros por pantalla
    z = None                      # se declara vacia por si ingresan valores no numericos
    if x.isdigit() and y.isdigit():
        z = float(x) - float(y)
        return z
result2 = substraction()
print(f'La resta es ', result2)

# multiplicacion
def multiplication(a,b):
    print(a * b)    # Sin return la funcion NO devuelve resultado
multiplication(2, 6)

# division
def division(a,b):
    if b == 0:
        print('No se puede dividir por 0')
    else:
        print(a / b)
division(2, 6)
print()

# potencia 
def power(x,w,y,z):
    x = input('Ingrese x ')
    w = input('Ingrese w ')
    y = input('Ingrese y ')
    z = input('Ingrese z ')
    a = None
    if x.isdigit() and w.isdigit() and y.isdigit() and z.isdigit():
        x = float(x)
        w = float(w)
        y = float(y)
        z = float(z)
        x = x**x
        w = w**w
        y = y**y
        z = z**z
        return x,w,y,z
    return a
result3 = power(2,3,4,5)
print(result3)
print()

# verificar decimales
def es_flotante(variable):
	try:
		float(variable)
		return True
	except:
		return False


datos = ['123', 'asd', 'eeee', '----', '-5', '1.60']
for dato in datos:
	print('¿"{}" es un flotante? {}'.format(dato, es_flotante(dato)))

    
# FUNCIONES ALEATORIAS DE PYTHON
# randint, choice
from random import randint, choice

a = print(choice(['hola','mundo','feliz','triste']))
b = print(randint(1,12))
print()
for i in range(3):
    dice1 = print(randint(1,6))
    dice2 = print(randint(1,6))
    print()
