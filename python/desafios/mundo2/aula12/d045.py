from random import randint #importar modulos
itens = ['Pedra', 'Papel', 'Tesoura']#colocar opção
computador = randint (0, 2) #colocando para o computando escolher
# Para pegar str usa choice 
#menu
print ('''Suas opcões:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int (input ('Qual sua opção? ')) #entrada de opcao

if jogador != 1 and jogador != 2 and jogador != 3:
  print ('tente novamente!!')
  jogador = int (input ('Qual sua opção? '))

print ('-=' * 30)
print (f'O computador escolheu {itens[computador]}')
print (f'Jogando jogou {itens[jogador]}')
print ('-=' * 30)

if computador == jogador:
  print ('EMPATE')
else:
  if computador == 0: #computador jogou pedra
    # if jogador == 0: #PEDRA
    #   print ('EMPATE')
    if jogador == 1: #PAPEL
      print ('JOGADOR VENCEU')
    elif jogador == 2: #TESOURA
      print ('JOGADOR PERDEU')
    else: #SEM NUMERO
      print ('jogada invalida')

  elif computador == 1: #computador jogou papel
    if jogador == 0: #PEDRA
      print ('JOGADOR PERDEU')
    # elif jogador == 1: #PAPEL
    #   print ('EMPATE')
    elif jogador == 2: #TESOURA
      print ('JOGADOR VENCEU')
    else: #SEM NUMERO
      print ('jogada invalida')

  elif computador == 2: #computador jogou tesoura
    if jogador == 0: #PEDRA
        print ('JOGADOR VENCEU')
    elif jogador == 1: #PAPEL
      print ('JOGADOR PERDEU')
    # elif jogador == 2: #TESOURA
    #   print ('EMPATE')
    else: #SEM NUMERO
      print ('jogada invalida')
