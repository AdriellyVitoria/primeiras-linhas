n = str (input('qual o seu nome completo? ')).strip()
nome = n.split()
print ('Muito prazer em te conhecer!')
print (f'Seu primeiro nome é {nome [0]}')
print (f'Seu nome último nome é: {nome [len(nome)-1]}')