# PROGRAMA PARA CREACION DE LISTA CON 5 ELEMENTOS
# INGRESO DE DATOS
print('Escribe 5 palabras para crear tu colección')
w1 = input('1: ')
w2 = input('2: ')
w3 = input('3: ')
w4 = input('4: ')
w5 = input('5: ')

# CREACIÓN DE LISTA
list = []
list.append(w1)
list.append(w2)
list.append(w3)
list.append(w4)
list.append(w5)
print(f'Esta es tu lista {list}\nQué deseas hacer con ella?')

# DECISIÓN DEL CLIENTE AGREGAR - BORRAR - CERRAR
decision = input('Agregar un elemento (a)\nBorrar un elemento (b)\nCerrar programa (c)\n')
while decision == 'a' or decision == 'A' or decision == 'b' or decision == 'B':
    if decision == 'a' or decision == 'A':
        w6 = input('Agrega un elemento: ')
        list.append(w6)
        print(f'Tu lista actualizada\n{list}\nQue deseas hacer?')
        decision = input('Agregar un elemento (a)\nBorrar un elemento (b)\nCerrar programa (c)\n')
    if decision == 'b' or decision == 'B':
        print(list)
        eliminar = input('Elimina un elemento por su nombre tal cual esta en la lista: ')
        if eliminar in list:
            list.remove(eliminar)
            print(f'Tu lista actualizada\n{list}\nQue deseas hacer?')
            decision = input('Agregar un elemento (a)\nBorrar un elemento (b)\nCerrar '
                             'programa (c)\n')
        else:
            decision = input('Ese valor no existe en la lista, que quieres hacer?\nAgregar un '
                             'elemento (a)\nBorrar un elemento (b)\nCerrar programa (c)\n')
if decision == 'c' or decision == 'C':
    print('Sesión finalizada\nGracias')
else:
    print('Error, intenta de nuevo')