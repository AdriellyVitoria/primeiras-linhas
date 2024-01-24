from random import randint
numero = int (randint(1, 10))
ganho = 0

while True:
  print ('-=' * 30)
  print ('VAMOS JOGAR PAR OU IMPAR')
  print ('-=' * 30)

  jogador = int (input ('Digiter um valor: '))
  opcao = input ('Par ou Impar? [P/I]').upper()
  soma = jogador + numero

  if soma  % 2 == 0 and opcao == 'P':
    print (f'Voce jogou {jogador} e o computador {numero}. total de {soma} DEU PAR, vc ganhou')
    ganho += 1

  elif soma % 2 == 1 and opcao == 'I':
    print (f'Voce jogou {jogador} e o computador {numero}. total de {soma} DEU IMPAR, vc ganhou')
    print ('Vamos jogar novamente...')
    print ('-=' * 30)

  else:
    print (f'Voce jogou {jogador} e o computador {numero}. total de {soma}')
    print ('-=' * 30)
    print (f'GAME OVER !! você venceu {ganho}')
    break


  


