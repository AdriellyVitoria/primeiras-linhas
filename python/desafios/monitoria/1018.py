nota = int(input())

# separar as notas 100 até 1 real
#Começar separando as notas de 100
notaValor100 = int (nota / 100)
print( f"tenho {notaValor100} notas de 100 reias")
#para prosseguir vc pegar o valor completo e diminuir pelas as notas de 100 separando assim:
sobrou = nota - (notaValor100 * 100)
print(f"ficou {sobrou}")
# notaTotal100 = nota % 100

notaValor50 = nota / 50
notaTotal50 = nota % 50
notaValor20 = nota / 20
notaTotal20 = nota % 20
notaValor10 = nota / 10
notaTotal10 = nota % 10
notaValor5 = nota / 5
notaTotal5 = nota % 5
notaValor2 = nota / 2
notaTotal2 = nota % 2
notaValor1 = nota / 1
notaTotal1 = nota % 1

# print('{} nota(s) de R$ {},00'.format(notaValor100, notaTotal100))
# print('{} nota(s) de R$ {},00'.format(notaValor50 , notaTotal50))
# print('{} nota(s) de R$ {},00'.format(notaValor20, notaTotal20))
# print('{} nota(s) de R$ {},00'.format(notaValor10, notaTotal10))
# print('{} nota(s) de R$ {},00'.format(notaValor5, notaTotal5))
# print('{} nota(s) de R$ {},00'.format(notaValor2, notaTotal2))
# print('{} nota(s) de R$ {},00'.format(notaValor1, notaTotal1))

#576
# 5 nota(s) de R$ 100,00
# 1 nota(s) de R$ 50,00
# 1 nota(s) de R$ 20,00
# 0 nota(s) de R$ 10,00
# 1 nota(s) de R$ 5,00
# 0 nota(s) de R$ 2,00
# 1 nota(s) de R$ 1,00