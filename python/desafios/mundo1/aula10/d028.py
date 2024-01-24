from random import randint
número = int (randint(0,5))
jogando = int(input('Vou pensar em um número entre 0 e 5. tente adivinhar em qual número estou pensando: '))
if jogando == número :
 print (f'Você GANHOU! eu pensei no {número}')   
else: 
  print(f' GANHEI! eu pensei no número {número}')
