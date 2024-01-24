#desenvolva um programa q leia o primeiro termo e a razão de uma PA. no final, mostre os 10 primeiros termos dessa progressão. 

primeiro = int (input ('Primeiro termo: ')) #entrada do primeiro termo
razao = int (input ('Razão: ')) #entrda da razão
decimo = primeiro + (10 - 1) * razao #pegar os 10 primeiros numeros
for c in range (primeiro, decimo + razao, razao): #vai do primeiro numero pulado de acodor com a razao até a razao
  print (c, end="-> ") #saida dos numeros
print ('fim') #saida do fim