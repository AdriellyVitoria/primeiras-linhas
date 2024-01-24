#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = menor = 0 #acumulador
for c in range (1, 6): #vai de 1 ate 6
  peso = float (input (f'Digite o peso da {c} pessoa: ')) #entrada dos pesos
  if c == 1: 
    maior = menor = c 
  else: #verificar quem é o maior e menor
    if peso > maior:
      maior = peso
    if peso < menor:
      menor = peso

#saida
print (f'O maior peso lido foi de {maior:.1f}Kg')
print (f'Omenor peso lido foi de {menor:.1f}Kg')


