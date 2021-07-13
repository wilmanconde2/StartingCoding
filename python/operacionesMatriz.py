from random import randint
import numpy as np

matriz1 = []        # se inicializa la lista matriz1 vacia
numf = input('Ingresa numero de filas\n-> ')
numc = input('Ingresa numero de columnas\n-> ')
numf = int(numf)
numc = int(numc)
print()
print('Matriz1')
for raw in range(numf):     # se recorren la filas en el rango que queremos  (0,10) o (10)
    fila = []               # por cada recorrido se crea una fila vacia
    for column in range(numc):     # se recorren las columnas en el rango que queremos  (1, 6) o (5)
        # fila.append(input('Ingresa numero'))        # agrega los elementos el usuario
        fila.append(randint(1,100))         # agraga elementos aleatorios de 1 a 100 con randint
    matriz1.append(fila)         # se agregan los elementos a la matriz
for i in matriz1:       # imprime la lista como matriz multidimensional
    print(i)
print()

matriz2 = []        # se inicializa la lista matriz2 vacia
print('Matriz 2')
for raw in range(numf):     
    fila = []            
    for column in range(numc): 
        #   fila.append(input('Ingresa numero')     # agrega los elementos el usuario
        fila.append(randint(1, 100))
    matriz2.append(fila)    
for i in matriz2:      
    print(i)
print()

num1 = np.array(matriz1)        # utilizamos libreria numpy para poder operar matrices
num2 = np.array(matriz2)
print(f'matriz 1 + matriz 2\n{num1+num2}\n')        # suma matrices
print(f'matriz 1 - matriz 2\n{num1-num2}\n')        # resta matrices
print(f'matriz 1 * matriz 2\n{num1*num2}\n')        # multiplicacion matrices

escalar = input('Elige un numero para multiplicar las matrices (escalar)\n-> ')     # se pide entero
if escalar.isdigit():
    escalar = int(escalar)
    print(f'matris 1 * escalar {escalar}\n{num1*escalar}\n')        # multiplicacion por escalar
    print(f'matris 2 * escalar {escalar}\n{num2*escalar}\n')        # multiplicacion por escalar
else:
    print('Dato invalido, gracias')