import numpy as np

matriz1 = [[3, 6, 8], [7, 3, 9], [1, 8, 5]]

matriz2 = [[4, 7, 9], [2, 0, 5], [7, 3, 1]]

print('Matriz 1')
for i in matriz1:       # imprime el arreglo como matriz multidimensional
    print(i)
print()

print('Matriz 2')
for i in matriz2:       # imprime el arreglo como matriz multidimensional
    print(i)
print()

matriz1 = np.array(matriz1)
num1 = matriz1[:, 2]        # el parametro [:] busca en todas las filas de la lista [#fila, #posición]
print(f'columna #3 matriz1 = {num1}')

matriz2 = np.array(matriz2)
num2 = matriz2[:, 0]        # el parametro [:] busca en todas las filas de la lista [#fila, #posición]
print(f'columna #1 matriz2 = {num2}')

mult = num1 * num2
print(f'multiplicacion {mult}')
print()

matriz1 = np.array(matriz1)
num1 = matriz1[2, 1]        # [2,1] busca el elemento de la fila 3 y posición 2
print(f'Elemento de matriz1 - fila 3, posición 2 -> {num1}')

matriz2 = np.array(matriz2)
num2 = matriz2[1, 2]        # [1,2] busca el elemento de la fila 2 y posición 3
print(f'Elemento de matriz2 - fila 2, posición 3 -> {num2}')
