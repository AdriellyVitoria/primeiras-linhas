mulher = idade = m = 0
while True:
  print ('-' * 50)
  print ('CADASTRE UMA PESSOA')
  print ('-' * 50)

  idade = int (input ('idade: '))
  sexo = input ('Digite seu sexo: [F/M]').upper()[0]

  while sexo != 'F' and sexo != 'M':
    print ('ERRO!!!')
    sexo = input ('Digite seu sexo: [F/M]').upper()
  print ('=-' * 50)

  continuar = input ('Gostaria de continuar? [S/N] ').upper()
  while continuar != 'N' and continuar != 'S':
      print ('ERRO!!!')
      continuar = input ('Gostaria de continuar? [S/N]').upper()
  print ('-=' * 50)

  if idade >= 18:
    idade += 1

  if sexo == 'M':
    m += 1

  if sexo == 'F' and idade > 20:
    mulher += 1

  if continuar == 'N':
    print ('====== FIM DO PROGRAMA ======')

    print(f'''
    Total de pessoa (s) com mais de 18 anos {idade}
    ao todo temos {m} homem (ns) cadastrados
    E temos {mulher} mulher (es) com menos de 20 anos''')
    break
