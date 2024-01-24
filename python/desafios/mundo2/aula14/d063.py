#programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de fibonacci.
print ('~~'*30)
print ('Sequência de Fibonacci')
print ('~~'*30)
numero =  int (input('Quantos termos você quer mostrar? ')) #entrada
t1 = 0 #começar no 0
t2 = 1 #comer nop 1
print (f'{t1} -> {t2}', end='') 
contagem = 3 #
while contagem <= numero:
  t3 = t1 + t2 #somar para pegar o proximo numero
  print (f'-> {t3}', end='') #saida
  t1 = t2 #somar 
  t2 = t3 #somar
  contagem += 1 #aumentar o contador
print ('-> FIM') #saida
