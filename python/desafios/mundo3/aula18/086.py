lista = []
giros = 0
for i in range (3):
    for j in range (3):
        numero = int (input (f'Digite um valor para [{i}, {j}]: '))
        lista.append(numero)

for a, b in enumerate(lista):
    print (f'[ {b} ]',end='')
    giros += 1
    if giros == 3:
        print ()
        giros = 0
