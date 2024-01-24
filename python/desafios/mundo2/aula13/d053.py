#um programa q leia uma frase qualquer e diga se ela é um palindromo, desconsierando os espaços

frase = input ('Digite uma frase: ').strip().upper()#tire os espacos e coloquei tudo para maiuculas
#tirar os espaços da frase
palavra = frase.split() #esparei as palavras
junto = ''.join(palavra) #juntei tudo em uma str só

#fiz o inverso troquei as letras
# inverso = ''
# for letra in range (len(junto) - 1, -1, -1):
#   inverso += junto [letra]

inverso = junto[::-1] #pode-se fazer isso para nãop usar o for (fartiamento)

print (f'O inverso de {junto} é {inverso}') #sainda

if inverso == junto: #verificar se as frases não mudam de tras para a frente
  print ('Temos um palindromo') #saida
else:
  print ('A frase digitanda não é um palíndromo')#saida
