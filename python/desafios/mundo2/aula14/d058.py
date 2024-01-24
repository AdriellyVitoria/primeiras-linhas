#o computando vai pensar em um número de 1 á 10, e vc tem q acertar qual é esse número.

from random import randint #modulo para colocar o codigo par pegar um numero
from time import process_time_ns
número = int (randint(1, 10)) #de 1 a 10
print('pensei em um número de 1 a 10...') #saida 
acertos = False 
palpites = 0 #contador
while not acertos : #só vai parar quando o jogando acertar
  jogada = int (input('Tente adivinhar em qual número eu pensei: ')) #entrasa
  palpites += 1 #aumento no contador
  if número == jogada: #se jogando acertar
    print (f'Parabéns, vc acertou em {palpites} tentativas') #saida
    acertos = True #para parar
  else: 
      if jogada < número: #se jogou um numero menor
        print ('Mais... tente novamente: ') #saida
      elif jogada > número: #se jogou um numero maior
        print ('Menos... tente novamente: ') #saida
       