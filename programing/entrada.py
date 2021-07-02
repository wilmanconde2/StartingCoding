entero = int(input('Ingresa un entero '))       # pide a usuario un entero
flotante = float(input('Ingresa un flotante '))  # pide a usuario un decimal
char = input('Ingresa un caracter ')            # pide a usuario un caracter
cadena = input('Ingresa una cadena ')           # pide a usuario una cadena
booleano = input('True o False ')               # pide a usuario un booleano
if booleano == 'True' or booleano == 'true':       # transforma cadena en booleano
    booleano = True
elif booleano == 'False' or booleano == 'false':
    booleano = False
else:
    print('Invalid booleano')                   # imprime resultados de lo ingresado
print(f'Ingresaste\nEntero {entero}\nFlotante {flotante}\nBooleano {booleano}\nCaracter {char}\nCadena {cadena}')
