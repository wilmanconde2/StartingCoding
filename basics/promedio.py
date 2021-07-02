total = 0
contador = 0
while True:
    nota = input('Ingresa un numero: ')
    if nota == 'fin' or nota == 'FIN':
        break
    if nota.isnumeric():
        nota = float(nota)
        total = total + nota
        contador += 1
    
        promedio = total / contador
        print('promedio: ', promedio)
    else:
        print('no valido')