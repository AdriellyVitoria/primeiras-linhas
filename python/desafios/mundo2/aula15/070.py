total = caro = barato = 0
while True:
  print ('=' * 50)
  print ('LOJA DO BARATÃO')
  print ('=' * 50)

  produto = input ('Nome do produto: ')
  preco = int (input ('Preço: R$'))
  continuar = input ('Quer continuar:[S/N] ').upper()[0]

  while continuar != 'S' and continuar != 'N':
    print ('ERRO!!')
    continuar = input ('Quer continuar:[S/N] ').upper()[0]
  total += preco

  if preco >= 1000:
    caro += 1  

  if barato < preco or preco < barato :
    barato = preco
    nome = produto
    
  if continuar == 'N':
    print (f'''
    O total de compras foi R${total:.2f}
    temos {caro} produtos custando mais de R$1000,00
    O produto mais barato foi {nome} que custa R${barato}''')
    break
