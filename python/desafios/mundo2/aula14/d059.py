'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

numero1 = int (input('Digite seu primeiro número: ')) #entrada
numero2 = int (input('Digite seu segundo número: ')) #entrada
menu = 0 #contador
while menu != 5: #só vai parar quando for 5
  #menu
    print ('''O que vc gostaria de fazer:
    [1] Soma
    [2] Multiplicar
    [3] Maior
    [4] Novos número
    [5] Sair do programa
    ''')
    menu = int (input ('Qual opção vc deseja escolher? ')) #entrad de escolhar

    if menu == 1: #se for igual a 1 vai soma
      print (f'o número {numero1} + {numero2} vai dá {numero1 + numero2}') #saida
      print ('-=' * 23)  #para separar

    elif menu == 2: #se for igual a 2 vai multiplicar
      print (f'O número {numero1} x {numero2} vai dá {numero1 * numero2}') #Saida
      print ('-=' * 23) #para separar
    elif menu == 3: #se for ig8ual a 3 vai pegar o maior numero
      if numero1 > numero2:
        print (f'o número {numero1} é o maior.') #Saida
      elif numero1 < numero2:
        print (f' O número {numero2} é o maior.') #Saida
      elif numero1 == numero2:
        print ('Os números são iguais.')#Saida
      print ('-=' * 23) #para separar

    elif menu == 4: #se for igual a 4 pegar novos numeros
     print ('Informe seus números novamnete:')
     numero1 = int (input('Digiter seu primeiro número: ')) #entrada
     numero2 = int (input('Digiter seu segundo número: ')) #entrada
     print ('-='*23) #para separar

    elif menu == 5: #para acarber o programa
     print ('Finalizado... Volter sempre') #Saida
     print ('-='*23) #para separar
    else:
      print ('opção invalida, tente novamente.') #Saida
      print ('-='*23) #para separar
