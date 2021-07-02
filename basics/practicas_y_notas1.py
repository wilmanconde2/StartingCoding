# IMPRIMIR EN PANTALLA
print('Hola Mundo')
print()
# SALTO DE LINEA \n
print('Mi nombre es Wilman\nMi apellido Conde')
print()

# TIPOS DE DATOS EN PYTHON
    # Numericos, Textos y Booleanos

# CONCATENAR con coma ,
name = 'Thiago Conde'
print('Mi nombre es',name)
print()

# COMENTARIO DE UNA LINEA CON #
# COMENTARIOS MULTIPLES LINEAS CON COMILLAS SIMPLES ''' '''
'''
    todo el comentario entre las comillas simples
'''

# OPERADORES ARITMETICOS
'''
    + suma - resta * multiplicacion / division % modulo // division redondeada ** potencia
    (/) la division devuelve numero decimal
    (%) el modulo devuelve el residuo de una division
    (//) la division devuelve numero redondeado
    (**) exponenciacion

    prioridad de operadoress aritmeticos
    1ro ()
    2do **
    3ro *, /, %
    4to +, -
'''
a = 10
b = 3
add = a+b
subt = a-b
mult = a*b
div1 = a/b
div2 = a//b
mod = a%b
pow = a**b
print(f'a= {a} b= {b}')
print(f'suma {add} resta {subt} multiplicación {mult} división {div1} \n'
      f'division redondeada {div2} modulo(residuo) {mod} exponente a**b {pow}')
print()

# OPERADORES RELACIONALES (menos prioridad que operadores aritmeticos)
'''    
    > mayor que
    < menor que
    >= mayor o igual
    <= menor o igual
    != diferente
    == igualdad
'''
a = 8
b = 12
greater = a>b
less = a<b
equal = a==b
problem = ((a+b<a-b)or(a*b+b/a)>(a**b))
print(f'a= {a} b= {b}')
print(f'Problema matemático (a+b<a-b)or(a*b+b/a)>(a**b)')
print(f'a>b {greater} a<b {less} a==b {equal} solución problema {problem}')
print()

# OPERADORES LOGICOS
''' 
    and conjuncion
    or disyuncion
    not negacion
    
    prioridad -> not, and, or
'''

# PRIORIDAD DE LOS OPERADORES EN GENERAL
'''
    ()
    **
    *, /, %
    +, -
    >, <, ==, >=, <=, !=
    not
    and
    or
'''

# OPERADORES DE ASIGNACION
''' 
    += suma en asignación
    -= resta en asignación
    *= multiplicaión en signación
    /= división en asignación
    **= exponenciacion en asignación
    %= modulo en signación
    //= división redondeada en asignación
'''
a = 0
print(f'a={a}')
a += 5  # suma en asignación
print(f'Suma de asignación a += 5 -> a={a}')
a -= 2  # resta en asignación
print(f'Resta de asignación a -= 2 -> a={a}')
a *= 10  # multiplicaión en signación
print(f'Multiplicación de asignación a *= 10 -> a={a}')
a /= 4  # división en asignación
print(f'Divisón de asignación a /= 4 -> a={a}')
a **= 3  # exponenciacion en asignación
print(f'Exponenciación de asignación a **= 3> a={a}')
a %= 4  # modulo en signación
print(f'Modulo de asignación a %= 4 -> a={a}')
