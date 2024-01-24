km = int (input('Em quantos km o seu carro estava? '))
multa = (km - 80) * 7
if km >= 80 :
 print (f'O senhor, devido a velocidade acima de 80km/h o senhor recebeu uma multa de {multa}')
else: 
  print (f'O senhor não recebeu nenhuma multa, pois o seu km {km} está abaixo de 80km. Obrigado,por digirir com segurança')