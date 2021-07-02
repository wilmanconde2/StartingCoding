from random import choice

paises = [['reino unido', 'paises bajos', 'turkia', 'suecia', 'noruega'],
          ['colombia', 'costa rica', 'jamaica', 'peru', 'salvador'],
          ['usa', 'mexico', 'rusia', 'dinamarca', 'iran'],
          ['argentina', 'chile', 'polonia', 'italia', 'suiza'],
          ['ecuador', 'brasil', 'alemania', 'iraq', 'irlanda']]
frutas = [['banano', 'arandano', 'tomate', 'maracuya', 'lichi'],
          ['fresa', 'melon', 'limon', 'naranja', 'uva'],
          ['pitalla', 'sandia', 'cereza', 'mora', 'manzana'],
          ['pera', 'guayaba', 'papaya', 'kiwi', 'mandarina'],
          ['granadilla', 'guanabana', 'chirimolla', 'grosella', 'zapote']]
generos = [['rock', 'salsa', 'vallenato', 'merengue', 'rap'],
           ['reggaeton', 'bachata', 'boleros', 'rancheras', 'baladas'],
           ['popular', 'electronica', 'heavy metal', 'tango', 'pop'],
           ['house', 'punk', 'disco', 'hip hop', 'rock en espanol'],
           ['clasica', 'blues', 'country', 'jazz', 'flamenco']]
animales = [['rinoceronte', 'tiburon', 'leopardo', 'pantera', 'pelicano'],
            ['perro', 'camaleon', 'leon', 'cabra', 'gallina'],
            ['cui', 'conejo', 'vaca', 'armadillo', 'guatin'],
            ['guagua', 'avestruz', 'jirafa', 'cisne', 'pato'],
            ['culebra', 'panda', 'tigre', 'elefante', 'mosca']]
peliculas = [['gladiador', 'dia de independencia', 'lord of the rings', 'soy leyenda', 'volver al futuro'],
             ['soul', 'parasitos', 'infinity war', 'coco', 'interstellar'],
             ['el lobo de wall street', 'django','intocable', 'origen', 'dark knight', ],
             ['infiltrados', 'batman begins', 'club de la pelea','salvando al soldado ryan', 'la vida es bella'],
             ['seven', 'cadena perpetua', 'la lista de schindler', 'el silencio de los inocentes', 'cars']]

def mostrar_titulo():
    '''
    input: 0 entradas
    process: muestra el titulo
    output: 0 salidas
    '''
    print('\n'*2)
    print('AHORCADO'.center(26,' '))
    print('   _____ '.center(26,' '))
    print('   |    |'.center(26,' '))
    print('   O    |'.center(26,' '))
    print('  /|\   |'.center(26,' '))
    print('  / \   |'.center(26,' '))
    print('________|'.center(26,' '))
    print()
    

def mostrar_menu():
    '''
    input: 0 entradas
    process: muestra el menu
    output: 0 salidas
    '''
    categoria = ['Paises','Frutas','Generos musicales','Animales','Peliculas','Finalizar']
    for n, m in enumerate(categoria,1):
        print(n, m)

def seleccionar_categoria_y_procesar():
    '''
    input: 1 entrada. Seleccion de categoria
    process: procesa seleccion categoria, crea variables
    output: 1 salida. Palabra a adivinar
    '''
    selection = input('Elige la categoria\n-> ')

    if selection == '1':        
        varAleatoria = choice(paises.pop())
        varAleatoria = varAleatoria.upper()
        return varAleatoria
    
    if selection == '2':
        varAleatoria = choice(frutas.pop())
        varAleatoria = varAleatoria.upper()
        return varAleatoria
    
    if selection == '3':
        varAleatoria = choice(generos.pop())
        varAleatoria = varAleatoria.upper()
        return varAleatoria
    
    if selection == '4':
        varAleatoria = choice(animales.pop())
        varAleatoria = varAleatoria.upper()
        return varAleatoria
    
    if selection == '5':
        varAleatoria = choice(peliculas.pop())
        varAleatoria = varAleatoria.upper()
        return varAleatoria
    
    if selection == '6':
        print('Gracias por participar')
        quit()
    
def jugar_ahorcado(varAleatoria):  
    '''
    input: letras ingresadas por usuario
    process: procesa las letras para encontrar la palabra secreta
    output: imagen de ahorcado, letras usadas y errores cometidos
    '''
    
    errores = 0
    progreso = []
    for i in range(len(varAleatoria)):
        progreso.append('_ ')
    
    palEspacios = []
    for i in varAleatoria:
        palEspacios.append(i + ' ')
    
    letrasUsadas = []
    
    while errores < 7:
        if errores == 0:
            print('\n'*50)
            print('   _____ '.center(26,' '))
            print('   |    |'.center(26,' '))
            print('        |'.center(26,' '))
            print('        |'.center(26,' '))
            print('        |'.center(26,' '))
            print('________|'.center(26,' '))
        elif errores == 1:
            print('\n'*50)
            print('   _____ '.center(26,' '))
            print('   |    |'.center(26,' '))
            print('   O    |'.center(26,' '))
            print('        |'.center(26,' '))
            print('        |'.center(26,' '))
            print('________|'.center(26,' '))
        elif errores == 2:
            print('\n'*50)
            print('   _____ '.center(26,' '))
            print('   |    |'.center(26,' '))
            print('   O    |'.center(26,' '))
            print('   |    |'.center(26,' '))
            print('        |'.center(26,' '))
            print('________|'.center(26,' '))
        elif errores == 3:
            print('\n'*50)
            print('   _____ '.center(26,' '))
            print('   |    |'.center(26,' '))
            print('   O    |'.center(26,' '))
            print('   |    |'.center(26,' '))
            print('  /     |'.center(26,' '))
            print('________|'.center(26,' '))
        elif errores == 4:
            print('\n'*50)
            print('   _____ '.center(26,' '))
            print('   |    |'.center(26,' '))
            print('   O    |'.center(26,' '))
            print('   |    |'.center(26,' '))
            print('  / \   |'.center(26,' '))
            print('________|'.center(26,' '))
        elif errores == 5:
            print('\n'*50)
            print('   _____ '.center(26,' '))
            print('   |    |'.center(26,' '))
            print('   O    |'.center(26,' '))
            print('  /|    |'.center(26,' '))
            print('  / \   |'.center(26,' '))
            print('________|'.center(26,' '))
        elif errores == 6:
            print('\n'*50)
            print('   _____ '.center(26,' '))
            print('   |    |'.center(26,' '))
            print('   O    |'.center(26,' ')) 
            print('  /|\   |'.center(26,' '))
            print('  / \   |'.center(26,' '))
            print('________|'.center(26,' '))
            print('Perdiste')
            errores = 0
            progreso = []
            palEspacios = []
            break
            
        print(''.join(progreso))
        print(f'Letras usadas: {letrasUsadas}')
        print(f'Te quedan {5 - errores} errores')
        letra = input('Ingresa una letra\n-> ').upper()
        if letra in letrasUsadas:
            print('Ya la usaste')
        else:
            letrasUsadas.append(letra.upper())
            
            error = True
            
            for i in range(len(varAleatoria)):
                if letra == varAleatoria[i]:
                    progreso[i] = letra + ' '
                    error = False
            
            if error:
                errores += 1 
            
        if palEspacios == progreso:
            print(f'La palabra era {varAleatoria}\nGANASTE!!')
            print('\n')
            errores = 0
            progreso = []
            palEspacios = []
            break
        
def reiniciar_juego():
    iniciar_programa()

def iniciar_programa():
    mostrar_titulo()
    mostrar_menu()
    varAleatoria = seleccionar_categoria_y_procesar()
    jugar_ahorcado(varAleatoria)
    reiniciar_juego()


iniciar_programa()