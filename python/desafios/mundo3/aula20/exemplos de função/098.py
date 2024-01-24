from time import sleep

def contagem (inicia, fim, passo):
  print ('-=' * 30)
  print (f'Contagem de {inicia} até {fim } em {passo}')
  if fim < inicia:
    passo *= -1

  for contagem in range (inicia, fim, passo):
    print (contagem, end=' ')
    
  


contagem (1, 10, 1)
contagem (10, -1, 2)

inicia = int (input ('Inicial: '))
fim = int (input ('Fim: '))
passo = int (input ('Passos: '))
contagem (inicia, fim, passo)
print ('\n')
print ('=-' * 30)
 