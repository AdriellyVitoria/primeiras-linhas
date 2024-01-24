valor = float (input('Qual o valor da casa que vc deseja comprar? '))
salario = float (input('Quanto vc ganhar atualmente:R$ '))
ano = int (input('Em quantos anos vc quer pagar? ')) 
valordisponivel = salario / 100 * 30
print (f'Vc vai em pagar em {ano * 12} parcelas, de { valor / (ano * 12):.2f} ')
if valor / (ano * 12) >= valordisponivel :
  print ('Infelizmnete, o emprestimo não será possive')
else :
  print ('Parabéns, vc vai conseguir o emprestimo!')
 