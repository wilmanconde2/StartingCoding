#  devuelta de compra
balon = 85000
pagoBalon = int(input('El balon cuesta 85000, con cuanto pagas? '))
devolucion = pagoBalon-balon
if pagoBalon < balon:
    print(f'Aun te faltan ${balon-pagoBalon}')
else:    
    print(f'Tu devuelta es de {devolucion}')