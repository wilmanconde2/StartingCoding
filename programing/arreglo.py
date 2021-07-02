from random import randint

lista = []                  # se inicializa lista vacia
numf = input('Ingresa numero de filas\n-> ')
numc = input('Ingresa numero de columnas\n-> ')
numf = int(numf)
numc = int(numc)
for fila in range(numf):       # se determina el numero de filas (elementos de la lista)
    fila = []               # por cada iteracion se genera una fila vacia (elemento de la lista vacio)
    for columna in range(numc):        # se determina el numero de columnas (cantidad de elementos por fila)
        fila.append(randint(1,10))      # se agregan numeros aleatorios a las filas creadas
    lista.append(fila)      # se agregan las filas creadas al arreglo vacio (lista)
print(f'Lista aleatoria\n-> {lista}')       # imprime la lista creada
print(f'Lista invertida\n-> {lista[::-1]})')        # imprime la lista de manera inversa