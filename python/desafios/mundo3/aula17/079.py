valores = []

while True:
    valor = int (input ('digite um numero, (999 para parar): '))
    if valor == 999:
        valores.sort()
        print (f'{valores}')
        print ('fim do programa')
        break
    else:
        if valor not in valores:
            valores.append(valor)
            print ('Valor adicionado com sucesso...')
        else:
            print ('Valor duplicado! Não vou adicionar...')
        