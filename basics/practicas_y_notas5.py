# LISTAS Y COLECCIONES
cities = ['Colombia', 'Francia', 'Perú', 'Ecuador', 'Mali', 'España', 'Inglaterra', 'Polonia']
print(f'Lista cities {cities}')
print(f'La cantidad de elementos en cities es -> {len(cities)}')  # imprime la cantidad de elementos que tiene la lista
print(f'Imprimiendo la posición 3 de cities -> {cities[3]}') # imprime la posición indicada (empieza desde 0)
print(f'Imprimiendo de atrás hacia adelante en la lista (-5) -> {cities[-5]}') # imprime de atrás hacia adelante
del cities[3] # elimina un elemento de la lista por la posición
print(cities)
cities.remove('España') # Elimina elemento directamente con el nombre
print(cities)
cities.append('Escocia') # Se añade un elemento al final de la lista
print(cities)
cities.insert(0, 'Honduras') # Se añade un elemento en la posición deseada
print(cities)
cities.pop() # Elimina el ultimo elemento de la lista
print(cities)
cities.pop(4)  # Elimina el elemento de la posición especificada
print(cities)
print(cities[:]) # Imprime la lista completa
print(cities[2:4]) # imprime los elementos entre las posiciones seleccionadas
print(cities[3:]) # Imprime desde la posición seleccionada hasta el final de la lista
print(cities[-4]) # Imprime del final hacia atrás la posición seleccionada
print(cities[::-1]) # Imprime la lista de atrás hacia adelante  
print('\n')

# DICCIONARIOS
dictionary = {'azul':'blue','amarillo':'yellow','rojo':'red'}
print(dictionary)
dictionary['verde'] = 'green' # Para insertar un elemento nuevo
print(dictionary)
dictionary['verde'] = 'GREEN' # Se puede modificar el VALOR de un elemento
print(dictionary)
del(dictionary['verde']) # Para eliminar un elemento
print(dictionary)
print(dictionary['rojo']) # Para mostrar el valor de una clave
print()

dictionary = {'Wilman':{'Edad':38,'Estatura':1.87},'Tania':{'Edad':26,'Estatura':1.57}}
                # Diccionario dentro de otro diccionario
print(dictionary)
print(dictionary['Tania']) # Para mostrar el valor de una clave
print()

team = {1:'Allison',5:'Ogbonna',2:'Sanchez',14:'Arnold',15:'Robertson',6:'Gattuso',
          7:'Ndidi',18:'James',22:'Overmars',10:'Bergkamp',9:'Stoikov'}
print(team[5]) # Si usamos este codigo, sale error si no exite el elemento y para el programa
print(team.get(5,'No existe un jugador con ese dorsal'))
print(team.get(17,'No existe un jugador con ese dorsal'))
    # Con .get si no existe el elemento, podemos dejar un mensaje y no saldría error de código
print()
print(10 in team) # Buscar en diccionario para saber si existe
print(28 in team) # Buscar en diccionario para saber si existe
print(team.keys()) # Con .keys muestra las claves del diccionario
print(team.values()) # Con .values muestra los valores del diccionario
print(team.items()) # Con .items muestra clave y valor
print(len(team)) # Muestra cuantos elementos hay en el diccionario
team.clear() # Limpia el diccionario
print(team)
