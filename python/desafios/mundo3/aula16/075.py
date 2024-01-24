nove = giro = 0
valor1, valor2, valor3, valor4 = map (int, input ('Digite 4 valores: ').split ()) #entrada

numero = (valor1, valor2, valor3, valor4) #tupla

print (f'{numero}\nO nove apareceu {numero.count(9)} vezes') #pegar os numeros 9

if 3 in numero: #verificar se tem numero 3
  print (f'O 3 foi digitando em {numero.index(3) + 1}° posicao')
else:
  print ('O numero 3 não foi digitando em nunhuma posição')

print (f'os valores pares digitandos foram', end = ' ') #saida dos numeros pares
for i in numero: #verificar se é par
  if i % 2 == 0: 
    print (i, end=' ')
 