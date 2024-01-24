lista = []

continuar = 'S'

while continuar == 'S':
        lista.append (int (input ('Digite um numero: ')))
        continuar = input ('Quer continuar [S/N] ').upper()
        while continuar != 'S' and continuar != 'N':
            print ('Erro tente novamente')
            continuar = input ('Quer continuar [S/N] ').upper()
        if continuar == 'N':
            print (f'A lista tem {len(lista)} numeros')
            lista.sort(reverse=True)
            print(lista)
            if 5 in lista:
                print ('O numero 5 está na lista')
            else:
                print ('O numero 5 não está na lista')
            print ('Fim do programar')
            break
