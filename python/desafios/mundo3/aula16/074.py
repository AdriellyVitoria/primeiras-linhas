from random import randint 
giros = maior = menor= 0 #contadores

while giros < 5: #vai gira 5 vezes
  giros += 1 #aumento no contador
  numero = int (randint(1, 10)) #escolher os numero de 1 a 5
  print (numero, end=' ') #saida, um ao lado do outro

  if menor == 0: #pegar o primeiro numero
    menor = numero

  if maior < numero: #pegar o maior numero
    maior = numero

  if menor >= numero: #pegar o menor numero 
    menor = numero

print (f'\nO maior numero é {maior}\nE o menor numero é {menor}') #saida
