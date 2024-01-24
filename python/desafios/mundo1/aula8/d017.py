from math import hypot
cateto = float ( input ('diga-me o número do Cateto oposto '))
adjacente = float (input (' diga-me um número do cateto Adjacente '))
hipotenusa = hypot( cateto, adjacente )
print (f' a soma do {cateto} mais {adjacente} é igual a {hipotenusa}')

'''co = float (input('Comprimento do cateto oposto: '))
ca = float (input('Comprimento do cateto adjacente: '))
hi = ((co ** 2 + ca ** 2) ** 1/2)
print (f'A hipotenusa vai medir {hi:.2f}')'''