cedulas_50 = cedulas_20 = cedulas_10 = cedulas_1 = resto = 0
while True:
  print ('=' * 50)
  print ('BANCO ADRIELLY')
  print ('=' * 50)
  valor = int (input ('Qual o valor a ser retirando: R$'))
  while resto == 0:
    valor -= 50

  print (f'''Total de {cedulas_50} cédulas de R$50
  Total de {cedulas_20} cédulas de R$20 
  Total de {cedulas_10} cédulas de R$10
  Total de {cedulas_1} moedas de R$1
  {valor}''')
  