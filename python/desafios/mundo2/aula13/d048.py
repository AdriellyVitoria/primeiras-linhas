#soma todos os numeros ímpares que são múltiplos de três a que se encontram no intervalo de 1 a 500:

s = giros = 0 #contadores
for c in range (0, 500, 3): #de 1 a 500 pulando em 3 em 3
  if c % 2 != 0 : #pegar os numeros impar
    giros += 1 #contador
    s += c #acumulador
print ('=-'*20) #para dividir
print (f'A soma de todos os {giros} valores solicitados é {s}') #saida