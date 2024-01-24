#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valo
contador = giros = maior = menor = 0

while True:
  giros += 1
  numero = float (input ('Digite um numero, [para parar digite 999] '))#entrada
  if numero == 999:
    break
  contador += numero #aculumando 
  saida = contador / giros #media
  if giros == 1:
    maior = numero
    menor = numero
  if numero > maior:
    maior = numero
  if numero < menor:
    menor = numero
  
print (saida, menor, maior)




