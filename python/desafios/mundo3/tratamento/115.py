print ('-' * 30)
print ('      MENU PRINCIPAL      ')
print ('-' * 30)

print('1 - Ver pessoas cadastradas\n2 - Cadastrar nova pessoa\n3 - Sair do sistema')
lista = []

opcao = int (input('Opção: '))

while opcao != 3:
    try:  
        if opcao == 1:
            print (f'{lista}')
        elif opcao == 2:
            nome = input ('Digite o nome da pessoa: ')
            lista.append(nome)
        elif opcao == 3:
            print('fim do programar... Até logo')


    except:
        print('ERRO: por favor, digite um numero inteiro válido')
    