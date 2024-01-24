#um programa q leia um numero inteiro e diga se ele é ou não um número primo (numero primo é aquele que é SÓ divindido por 1 e por ele mesmo. )
numero = int (input ('Digite um nemro: ')) #entrada de numero
total = 0 #contador
for c in range (1, numero + 1): #de ir ateó numero digitando
  if numero % c == 0: #verificar se é primo
    print ('\033[33m', end=' ') #mudar a cor é colocar ops numeros na mesma linha
    total += 1 #aumentar o contador
  else:
    print ('\033[31m', end=' ')#mudar a cor é colocar ops numeros na mesma linha
  print (c,end=' ') #saida de todos os numeros
print (f'\n\033[m0 numero {numero} foi divisível {total} vezes') #nsaida de quantas as vezes o numero foi divisivel
if total == 2: #verificar ser é primo
  print ('E por isso que é PRIMO!') #saida falando q é primo
else:
  print ('E por isso que ele NÃO é primo') #saida dissendo q não é primo
  