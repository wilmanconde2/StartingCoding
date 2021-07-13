# CICLOS PARA LISTAS Y MATRICES

list = [1, 2, 5, 7, 8, 4, 6, 89, 4, 34, 56, 435]
print(list[:])  # Imprime la lista completa
print(list[2:4])  # imprime los elementos entre las posiciones seleccionadas sin contar el ultimo
print(list[3:])     # Imprime desde la posición seleccionada hasta el final de la lista
print(list[-4])  # Imprime elemento de atrás hacia adelante la posición seleccionada
print(list[::-1])  # Imprime la lista de atrás hacia adelante
print('\n')
for i in range(0, len(list)):       # imprime cada elemento de la lista
    print(list[i])
print('\n')

for i in list:  # imprime cada elemento de la lista con espacio entre elementos
    print(i,' ',end='')
print('\n')

matriz = [[1, 2, 3, 4, 5, 6], [2, 3, 4, 4, 5, 4], [4, 3, 2, 5, 6, 4]]
print(matriz)
matriz[0][3] = 0        # para cambiar un elemento del arreglo [#fila][#columna] = #nuevo
matriz[1][1] = 0
matriz[2][4] = 0
print(matriz)
print('\n')

for i in matriz:
    print (i)             # imprime la lista como matriz multidimensional
print()

row = []
for i in matriz:
    row.append(i[2])        # imprimir columna de una matriz
print('columna 3 = ', row)
print()
    
for i in range(0, len(matriz)):
    fila = matriz[i]
    for j in range(0, len(fila)):       # imprime lista multidimensional
        print (fila[j])
    print()
    
