#um programa q leia o ano de nascimento de sete pessoas. no final mostre quantas pessoas ainda não atiginram a maioridade e quantas já são maiores.

from datetime import date #importar modulo
atual = date.today( ).year #saber o ano
totmaior =totmenor = 0 #contador
for pessoa in range (1, 8): #vai pegar 7 pessoas
  ano = int (input(f'Em que ano a {pessoa}ª pessoa nasceu? ')) #entrada dos anos
  idade = atual - ano #saber a idade
  if idade >= 18: #se tive mais de 18 anos
   totmaior += 1 #aumenatr no contador
  else:
    totmenor += 1#aumenatr no contado

#saida
print (f'Ao todo tivemos {totmaior} pessoas maiores de idade')
print (f'Ao todo tivemos {totmenor} pessoas menores de idade ')
