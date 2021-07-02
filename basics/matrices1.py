# INGRESO DE DATOS
print('Ingresa 18 números enteros para crear 2 matrices de 3x3')
w1 = input('1: ')
w2 = input('2: ')
w3 = input('3: ')
w4 = input('4: ')
w5 = input('5: ')
w6 = input('6: ')
w7 = input('7: ')
w8 = input('8: ')
w9 = input('9: ')
w10 = input('10: ')
w11 = input('11: ')
w12 = input('12: ')
w13 = input('13: ')
w14 = input('14: ')
w15 = input('15: ')
w16 = input('16: ')
w17 = input('17: ')
w18 = input('18: ')

#  CREACIÓN DE LISTA
list1 = [[0,0,0],[0,0,0],[0,0,0]]
list2 = [[0,0,0],[0,0,0],[0,0,0]]
list1[0][0] = w1
list1[0][1] = w2
list1[0][2] = w3
list1[1][0] = w4
list1[1][1] = w5
list1[1][2] = w6
list1[2][0] = w7
list1[2][1] = w8
list1[2][2] = w9
list2[0][0] = w10
list2[0][1] = w11
list2[0][2] = w12
list2[1][0] = w13
list2[1][1] = w14
list2[1][2] = w15
list2[2][0] = w16
list2[2][1] = w17
list2[2][2] = w18

print()
print('Matriz 1')
for i in list1:
    print(i)
print()

print('Matriz 2')
for i in list2:
    print(i)
print()