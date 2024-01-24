listados = ('Lápis', 1.75, 'borrachas', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

giros = -1
cont = -2
for compras in (listados):
  giros += 2
  cont += 2
  c = "."
  print (f'{listados [cont]:.<30} R$ {listados[giros]:>7.2f}')
print ('=-' * 30)
