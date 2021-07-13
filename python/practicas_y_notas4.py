# BUCLE WHILE (puede ser infinito)
# programa ejemplo para raíz cuadrada
import math

num = int(input('Digita un número '))
while num < 0:
    print('ERROR, debe ser un número positivo')
    num = int(input('Digita un número'))
print(f'La raíz cuadrada de {num} es {math.sqrt(num):.2f}')
print()

# BUCLE FOR recorre todos los elementos (bucle finito)
# listas [] tuplas () diccionarios {} conjuntos {} colecciones [] y cadenas
list = [4,74,2,'Will',43,'Thiago']
for i in list:
    print(i)
print()

dictionary = {'Wilfer':38,'Tania':26,'Thiago':2}
for clave,valor in dictionary.items(): # .items permite recorrer el diccionario completo
    print(f'{clave} -> {valor}')
print()

name = 'Wilman'
for i in name:
    print(i)
for i in name:
    print(i,end=' * ') # end= agrega lo que esta entre parentesis y elimina salto de linea