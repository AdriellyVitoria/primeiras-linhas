#melhora o des061, perguntando para o usauario se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
print ('Gerador de PA.')
print ('-='*23)
primeiro = int (input('Primeiro termo da PA: ')) #entrada
razao = int (input('Razão da PA: ')) #entrada
termo = primeiro 
contador = 1  #contador
total = 0 #acumulador
mais = 10 #só até 10
while mais != 0: #até mais for 0
  total += mais  #acumulador
  while contador <= total: #
    print (f'{termo} -> ', end='') #saida dos termos
    termo += razao #somar com a razao par pular
    contador += 1  #aumento no contador
  print ('PAUSA') #saida
  mais = int (input('Quantos termos você quer mostrar a mais? ')) #entrad de mais numeros 

print (f'Progressão finalizada com {total} termos mostrados ') #saida geral
