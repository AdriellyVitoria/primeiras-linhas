from itertools import count


num = int (input('diga um número entre 0 até 9999: '))
u = num // 1 % 10
d = num //10 % 10
c = num //100 % 10
m = num // 1000 % 10
print ('Analisando o número {num}: ')
print (f'Unidade: {u}')
print (f'Dezena: {d}')
print (f'Centena: {c}')
print (f'milha: {m}')
