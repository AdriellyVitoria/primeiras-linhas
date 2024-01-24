valor = float(input())

nota100 = valor // 100
nota050 = valor % 100 // 50
nota020 = valor % 100 % 50 // 20
nota010 = valor % 100 % 50 % 20 // 10
nota05 = valor % 100 % 50 % 20 % 10 // 5
nota02 = valor % 100 % 50 % 20 % 10 % 5 // 2
nota1 = valor % 100 % 50 % 20 % 10 % 5 % 2 // 1

centavos = valor % 100 % 50 % 20 % 10 % 5 % 2 % 1
centavos = round (centavos * 100, 0)
moeda050 = centavos // 50
moeda025 = centavos % 50 // 25
moeda010 = centavos % 50 % 25 // 10
moeda005 = centavos % 50 % 25 % 10 // 5
moeda01 = centavos % 50 % 25 % 10 % 5

print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(int(nota100)))
print('{} nota(s) de R$ 50.00'.format(int(nota050)))
print('{} nota(s) de R$ 20.00'.format(int(nota020)))
print('{} nota(s) de R$ 10.00'.format(int(nota010)))
print('{} nota(s) de R$ 5.00'.format(int(nota05)))
print('{} nota(s) de R$ 2.00'.format(int(nota02)))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(int(nota1)))
print('{} moeda(s) de R$ 0.50'.format(int(moeda050)))
print('{} moeda(s) de R$ 0.25'.format(int(moeda025)))
print('{} moeda(s) de R$ 0.10'.format(int(moeda010)))
print('{} moeda(s) de R$ 0.05'.format(int(moeda005)))
print('{} moeda(s) de R$ 0.01'.format(int(moeda01)))

#576.73
# NOTAS:
# 5 nota(s) de R$ 100.00
# 1 nota(s) de R$ 50.00
# 1 nota(s) de R$ 20.00
# 0 nota(s) de R$ 10.00
# 1 nota(s) de R$ 5.00
# 0 nota(s) de R$ 2.00
# MOEDAS:
# 1 moeda(s) de R$ 1.00
# 1 moeda(s) de R$ 0.50
# 0 moeda(s) de R$ 0.25
# 2 moeda(s) de R$ 0.10
# 0 moeda(s) de R$ 0.05
# 3 moeda(s) de R$ 0.01
