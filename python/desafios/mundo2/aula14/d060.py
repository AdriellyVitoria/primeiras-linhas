#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
#TEMOS A MANEIRA DE IMPORTA MÓDULO.
'''from math import factorial
numero = int (input('Diga um número para calcula o seu fatorial: '))
f = factorial (numero)
print (f'O fatorial de {numero} é {f}')'''

#TEMOS DE REAILIZAR TODA A CONTA:
n = int (input('Digite um número para calcular seu Fatorial: '))#entrada
c = n #vai comer pelo o numero digitando
f = 1 #
print (f'Calculando {n}! =', end=' ') #saida
while c > 0:
  print(f' {c} ', end='') #saida
  print(' x ' if c > 1 else ' = ', end='') #saida
  f *= c
  c -= 1 

print (f'{f}') #saida

