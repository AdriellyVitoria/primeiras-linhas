# valores = []

# maior = menor =  0
# posicao1 = []
# posicao2 = []
# for i in range (0, 5):
  
#   valor = int (input ())
#   valores.append(valor)
  
#   if maior == 0 == menor:   
#     maior = valor
#     menor = valor
#   elif valor >= maior:
#     maior = valor
#     posicao1.append(i)
#     i += 1
#   elif valor <= menor:
#     menor = valor
#     posicao2.append(i)
#     i += 1 

# print (f'Os numero q vc digitou foi {valores}\nO maior valor é {maior} na posição {posicao1}\nO menor valor é {menor} na posição {posicao2}')

lista = [] 
maior = menor = 0

for i in range (5):
  lista.append(int (input (f'Digite um número para a posição {i}: ')))

  if i == 0:
    maior = menor = lista[i]
  else:
    if lista[i] > maior:
      maior = lista[i]
    if lista[i] < menor:
      menor = lista[i]

print ('-=' * 30)
print (f'Os numero q vc digitou foi {lista}')

print (f'O maior valor é {maior} na posição ', end='')
for i, j in enumerate(lista):
  if j == maior:
    print (f'{i}...', end='')
print ()

print (f'O menor valor é {menor} na posição ', end='')
for i, j in enumerate(lista):
  if j == menor:
    print (f'{i}...', end='')
print ()
