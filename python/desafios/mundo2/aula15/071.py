cedulas_50 = cedulas_20 = cedulas_10 = cedulas_1 = 0
while True:
  print ('=' * 50)
  print ('BANCO ADRIELLY')
  print ('=' * 50)
  valor = int (input ('Qual o valor a ser retirando: R$'))
  while valor >= 50:
    valor -= 50
    resto = valor
    cedulas_50 += 1
  while resto >= 20:
    valor -= 20
    resto = valor
    cedulas_20 += 1
  while resto >= 10:
    valor -= 10
    resto = valor
    cedulas_10 += 1
  while resto >= 1:
    valor -= 1
    resto = valor
    cedulas_1 += 1
  print (f'''Total de {cedulas_50} cédulas de R$50
  Total de {cedulas_20} cédulas de R$20 
  Total de {cedulas_10} cédulas de R$10
  Total de {cedulas_1} moedas de R$1
  {valor}''')
  