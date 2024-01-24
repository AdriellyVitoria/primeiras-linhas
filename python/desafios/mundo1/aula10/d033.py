n1 = int (input('diga o primeiro número: '))
n2 = int (input('diga o segundo número: '))
n3 = int (input('diga o terceiro número: '))
menor = n1
if n2 < n1 and n2 < n3:
  menor = n2
if n3 < n1 and n3 < n2:
  menor = n3
maior = n1
if n2 > n1 and n2 > n3:
  maior = n2
if n3 > n1 and n3 > n2:
  maior = n3
print (f'O maior valor digitando foi: {maior}')
print (f'O menor valor digitando foi: {menor} ')