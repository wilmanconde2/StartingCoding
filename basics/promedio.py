def validar_decimal(num):
    while True:
        try:
            num_val = float(num)
            return num_val
        except (ValueError, TypeError):
            return "Error, ingrese un número"
total = 0
contador = 0
while True:
    nota = input('Ingresa un numero para hallar promedio o\nF para terminar\n-> ')
    if nota == 'f' or nota == 'F':
        break
    nota1 = validar_decimal(nota)
    if type(nota1) is float:
        total = total + nota1
        contador += 1
        promedio = total / contador
        print(f'{total} / {contador}')
        print('promedio: ', promedio)
    else:
        print('no valido')