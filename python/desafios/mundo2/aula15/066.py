giros = soma = 0 #contadores
while True:
  numero = int (input ('Digite um numero (parar em 999): ')) #entrada
  if numero ==  999: #condiçao para parar
    break
  giros += 1 #aumento no contador
  soma += numero #acumulador
print (f'A soma  dos {giros} valores, foi {soma}') #saida
