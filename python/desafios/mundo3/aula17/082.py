lista = []
par = []
impar = []

continuar = 'S'

while continuar == 'S':
    numero = int (input ('Digite um numero: '))
    lista.append(numero)
    continuar = input ('Quer continuar[S/N]: ').upper()

    while continuar != 'S' and continuar != 'N':
            print ('Erro tente novamente')
            continuar = input ('Quer continuar [S/N] ').upper()

    if continuar == 'N':
        break

for i in lista:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print (f'A lista completa é {lista}\nA lista de pares é {par}\nA lista de ímpares é {impar}')
    