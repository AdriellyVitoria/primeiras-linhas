numero = ('zero', 'um', 'dois', 'tres', 'quarto', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte') #tuplas

while True: #enquanto
  valor = int (input ('Digite um numero de 1 a 20: ( para parar aperte 999): ')) #entrada
  if valor == 999: #verificar a condição de parada
    print ('FIM DO PROGRAMA') #saida
    break 

  while valor < 0 or valor > 20: #verificar se o num é negativo ou maior q 20
    print ('ERRO, TENTE NOVAMENTE') #saida
    valor = int (input ('Digite um numero de 1 a 20: ')) #entrada

  print (f'O numero digitando foi {numero [valor]}') #saida
