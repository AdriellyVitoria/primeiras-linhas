#Faça um programa que leia o sexo de uma pesssoa, mas só aceirte os valores M e F, caso esteja errado, peça a digitação novamente até ter uma valor correto.

sexo = str (input('Qual seu sexo [F/M] ')).strip().upper()[0] #entrada, tira os espaços e colocar em letras maiuculas e pegar a primeira letra
while sexo not in 'MmFf' : #só vai parar quando pegar m ou f
   sexo = str (input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()#entrada, tira os espaços e colocar em letras maiuculas primeira letra

print (f'sexo {sexo} regristrado com sucesso!') #saida
