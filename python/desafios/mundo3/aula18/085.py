#uma lista com duas listas internas q são os impas e os pares

lista = []
valores = [[], []]
for i in range (7):
    numero = int (input(f'Digite um numero na posição {i}: '))

    if numero % 2 == 0:
        lista.append(numero)

        