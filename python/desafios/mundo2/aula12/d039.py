sexo = input ('Qual o seu sexo [F/M]: ').upper() #saber se é homem ou mulher 
if sexo == 'F': # se for mulher
  print ('vc não vai precisar se alistar') #saida
elif sexo == 'M': #se for homem
  from datetime import date #função para saber o ano atual
  atual = date.today().year #chamando a função para saber o ano
  ano = int (input('Em qual ano vc nasceu? ')) #entrada
  idade = atual - ano #sabendo a idade
  falta = 18 - idade  #saber quando tempo falta
  print (f'Quem nasceu em {ano} tem {idade} em {atual}')
  if idade == 18: #se for igual a 18 
    print (f'Vc deve se alista, pois já completou {idade} anos') #saida 
  elif idade < 18: #se tive a idade menor que 18
    print (f' Ainda faltam {falta} anos para o alistamento. Seu alistamento vai ser em {atual + falta} anos') #saida
  elif idade > 18: #tive mais que 18 anos
    falta = idade - 18
    print (f'Vc já passou do tempo de alista, pois sua idade é: {idade} anos, vc perdeu o tempo, pois, seu alistamento foi em {atual - falta} ') #saida
else: #se errar o sexo
  print ('Sexo invalindo. Tente novamente') #saida
