#um programa com a contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep  #importar modulo
for c in range (10, -1, -1 ): #vai de 10 até 0
  print (c) #saida
  sleep (0.5) #pausa de 1 segundo
print ('BUM, BUM... POOM') #saida dos fogos
