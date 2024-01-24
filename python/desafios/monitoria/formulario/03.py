#Um professor de matemática escreveu o seguinte código para verificar se um número é, ao mesmo tempo, multiplo de 2, 3 e 5, pórem o código não está funcionando corretamente, identifique o problema e rescreva o código de modo que cumpra o objetivo do professor.

valor = int ( input('Digite um número: '))

if valor % 2 == 0 and valor % 3 == 0 and valor % 5 == 0:
      # if valor % 3 == 0:
        # if valor % 5 == 0:
    print ('O número é simultaneamente multiplo de 2, 3 e 5')
else:
    print('O número não é simultaneamente multiplo de 2, 3 e 5')