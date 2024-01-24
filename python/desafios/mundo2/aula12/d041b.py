ano = int (input('Qual o ano que vc nasceu? '))
idade = 2022 - ano
if idade <= 9 :
  print (f'Se vc tem {idade} anos, vc é MIRIM')
elif idade <= 14:
  print(f'Se vc tem {idade} anos, vc é INFANTIL')
elif idade <= 19:
  print (f'Se vc tem {idade} anos, vc é JUNIOR') 
elif idade <= 20:
  print (f'Se vc tem {idade} anos, vc é SÊNIOR')
else:
  print(f'Se vc tem {idade} anos, vc é MASTER')
