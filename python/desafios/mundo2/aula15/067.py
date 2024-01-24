giros = 0
mutiplica = giros + 1
while True:
  valor = int (input ('Qual o numero que vc quer ver a tabuada: '))
  print ('-=' * 30)
  while giros <= 10:
    print (f'''{valor} X {giros} = {valor * giros}''')
    giros += 1
  print ('-=' * 30)

  if valor <= 0:
    print ('Tabuada, ENCERRADA. Volte sempre')
    break 

