lista = []
giros = soma = maior = soma2 = 0

for i in range (3):
    for j in range (3):
        numero = int (input (f'Digite um valor para [{i}, {j}]: '))
        lista.append(numero)

for a, b in enumerate(lista):
    print (f'[ {b} ]',end='')

    giros += 1
    if b % 2 == 0:
        soma += b

    if a == 2 or a == 5 or a == 8:
        soma2 += b

    if a == 3 or a == 4 or a == 5:
        if b > maior:
            maior = b

    if giros == 3:
        print ()
        giros = 0

print (f'soma dos valores pares {soma}\nA soma dos valores da terceira coluna é {soma2}\nO maior valor da segunda linha é {maior}')
