valor = int (input ('Qual o valor a ser pagor? ')) #entrada do valor
#menu
print ('''Qual a condição de pagamento:
[1] a vista no dinheiro/cheque
[2] a vista no cartão
[3] 2x no cartão
[4] 3x a 12x no cartão.''')
opção = int (input ('Qual é a opção? ')) #entrad de opçãó

if opção == 1: 
  print(f'A vista no dinheiro o produtor será {valor - (valor * 10) / 100:.2f}')
elif opção == 2:
  print(f'se passar no cartão a vista, fica de { valor - (valor * 5) / 100:.2f}')
elif opção == 3:
  print(f'Se passar no cartão em 2x, SEM JUROS fica de {valor / 2}')
elif opção == 4:
  parcelas = int (input ('Em quantas parcelas? '))
  if parcelas == 2:
    print(f'Se passar no cartão em 2x, SEM JUROS fica de {valor / 2}')
  elif parcelas >= 3:
    total = valor + (valor / 100 * 20)
    partotal = total / parcelas
    print(f'Se passar no cartão em {parcelas}X, terá juros, entt vai ficar de {partotal:.2f} COM JUROS')
    print (f'Sua compra de R${valor:.2f} vai custar R${total:.2f} no final.')
else:
  print ('Condição invalida, tente novamente!!')
  