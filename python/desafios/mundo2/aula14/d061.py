#ler o primeiro termo e a razão da PA, mostra os 10 primeiros termos da progressão.
print ('Gerador de PA.')
print ('-='*23)
primeiro = int (input('Primeiro termo da PA: ')) #entrada
razao = int (input('Razão da PA: ')) #entrada
termo = primeiro # vai recebeer o primeiro numero
contador = 1 #contador
while contador <= 10: #até chegar no 10
  print (f'{termo} -> ', end='') #saida
  termo += razao #pular para o proximo numero
  contador += 1 #aumentar o contador

print ('FIM!') #saida 
