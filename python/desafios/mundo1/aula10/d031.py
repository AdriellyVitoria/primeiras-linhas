distância = int (input ('Qual a distância que vc deseja viaja? '))
pequena = distância * 0.50
longa = distância * 0.45
if distância <= 200 :
 print(f' Sua viagem vai custar R${pequena}')
else:
 print (f'Sua viajem é muito longa, então sua passagem vai custar: R${longa}')
