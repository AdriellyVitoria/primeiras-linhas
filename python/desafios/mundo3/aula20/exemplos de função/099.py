def maior (maior):
  giros = 0
  maior = numero = 0
  valores = []

  while True:
    giros += 1
    if numero >= maior:
      maior = numero
    valores.append(numero)
    numero = int (input ('Digite um numero, para verifcar os numero [aperte 999] '))
      
    if numero == 999:
      print (f'Analisando os valores passados...\n{len(valores)} Foram imformados {giros - 1} valores ao todo.\nO maior valor informado foi {maior}')
      giros = 1
      maior = numero = 0

    elif numero == '':
      print ('encerrado o programa... volter sempre ')
  

maior (maior)
