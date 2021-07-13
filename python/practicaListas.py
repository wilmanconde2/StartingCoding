# ejercicios con listas

# crear lista con cantidad definida por usuario
# cantidadPalabras = int(input('Cuantas palabras tiene la lista\n-> '))
# for i in range(cantidadPalabras):
#     palabra = input('Escribe una palabra\n-> ')
#     lista.append(palabra)
# print(f'La lista creada es {lista}')

# contar las apariciones de un elemento en una lista
# lista = []
# cantidadPalabras = int(input('Cuantas palabras tiene la lista\n-> '))
# for i in range(cantidadPalabras):
#     palabra = input('Escribe una palabra\n-> ')
#     lista.append(palabra)
# print(f'La lista creada es {lista}')
# pal = input('Que palabra quieres buscar en la lista?\n-> ')
# can = lista.count(pal)
# print(f'La palabra {pal} se encuentra en la lista {can} veces')

# sustituir elemento de una lista en la misma posición
# lista = []
# cantidadPalabras = int(input('Cuantas palabras tiene la lista\n-> '))
# for i in range(cantidadPalabras):
#     palabra = input('Escribe una palabra\n-> ')
#     lista.append(palabra)
# print(f'La lista creada es {lista}')
# eliminado = input('Elemento que quiere sustituir?\n-> ')
# agregar = input('Elemento a ingresar\n-> ')
# for i in range(len(lista)):
#           if lista[i] == eliminado:
#               lista[i] = agregar
# # for n, i in enumerate(lista):             # enumera los elementos - otra manera de codigo - 
# #   if i == eliminado:
# #      lista[n] = agregar
# print(lista)

# borrar un elemento las veces que este en la lista
# lista = []
# cantidadPalabras = int(input('Cuantas palabras tiene la lista\n-> '))
# for i in range(cantidadPalabras):
#     palabra = input('Escribe una palabra\n-> ')
#     lista.append(palabra)
# print(f'La lista creada es {lista}')
# eliminado = input('Elemento que quiere eliminar?\n-> ')
# for i in range(len(lista)-1,-1,-1):     # se debe leer la lista de atras hacia adelante porque cada que borra un elemento
#   if lista[i] == eliminado:             # el rango cambiaria y mostraria error
#       del lista[i]
# print(lista)

# 