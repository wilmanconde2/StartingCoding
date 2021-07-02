# operadores de relación, aritméticos y booleanos
a = 16
b = 6
add = a+b
subt = a-b
mult = a*b
div = a/b
mod = a % b
div2 = a//b
pow = a**b
greater = a > b
less = a < b
equal = a == b
problem = ((a+b < a-b) or (a*b+b/a) > (a**b))
p1 = a*mult+div
p2 = a/mult+mod
p3 = b-a*div2+div
p4 = p1+p2*p3
p5 = p4/b+p1
p6 = p2/p4
p7 = p3+p5/a
print(f'a= {a} b= {b}')
print('problema matematico (a+b<a-b)or(a*b+b/a)>(a**b)')
print(f'a>b {greater} a<b {less} a==b {equal} solucion problema {problem}')
print(f'a= {a} b= {b}')
print(f'suma {add} resta {subt} multiplicacion {mult} division {div:.4f} \n'
      f'modulo(residuo) {mod} division redondeada {div2} exponente a**b {pow}\n')
print(f'Operaciones\n1 {p1}\n2 {p2}\n3 {p3}\n4 {p4}\n5 {p5}\n6 {p6}\n7 {p7}')