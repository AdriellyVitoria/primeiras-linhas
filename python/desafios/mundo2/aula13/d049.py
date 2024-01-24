#fazer uma tabuanda usando o laço for:
numero = int (input('Diga o número que vc deseja ver a tabuada: ')) #entrada do numero
for c in range (0, 10): #a tabuada de 1 a 10
  print (f'{numero} x {c + 1} = {numero * (c + 1)}') #saida da tabuada
  