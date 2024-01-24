soma_idade = maior_idade_homem = mulheres = 0 #contadores
nome_velho = '' #pegar o nome do homem mais velho
for p in range (1, 5): #vai de 1 até 4

  #entrada das imformações dos usuarios
  print (f'----- {p} PESSOA ----')
  nome = input ('Digite seu nome: ').strip ()
  idade = int (input ('Qual sua idade: '))
  sexo = input ('Seu sexo:[M/F] ').strip().upper()

  soma_idade += idade  #acumulador

  if p == 1 and sexo == 'M': #guarda a primeira idade do homem
    maior_idade_homem = idade #arquivou a idade 
    nome_velho = nome #e o nome do homem

  if sexo == 'M' and idade > maior_idade_homem: #verificar se a primeira idade é maior
   maior_idade_homem = idade #se não, trocar a idade pela a maior
   nome_velho = nome #e arquiva o nome tbm

  if sexo == 'F' and idade < 20: #pegar as mulheres qu tem menos de 20 anos
    mulheres += 1 #contador

#saidas
print (f'A media de idade do grupo é de {soma_idade // 4 :.1f}')
print (f'O homem mais velho tem {maior_idade_homem} e se chamar {nome_velho}')
print (f'Ao todo são {mulheres} mulheres com menor de 20 anos')
