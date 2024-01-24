#um programa que leia varios numeros int.o programa só vai paar quando o usuario digitar 999, que é a condição de parada no final mostre quantos numeros foram digitando e qual foi a soma entre eles (condiderando o flag)

numero = soma =  contador = 0 #contadores
while numero != 999: #ate o numero ser diferente de 999
  soma += numero #acumulador
  contador += 1 #contador
  numero = int (input('Digite um numero [parar digiter 999] ')) #entrada
print (f'voce digitou {contador} numeros, e a soma de todos os número é {soma}') #saida