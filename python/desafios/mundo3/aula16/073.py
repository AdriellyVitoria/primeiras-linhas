times = ('palmeiras', 'internacional', 'flamengo', 'fluminense', 'corinthians', 'athletico', 'atletico', 'sao paulo', 'fortaleza', 'botafogo', 'america', 'santos', 'goias', 'red bull', 'coritiba', 'cuibá', 'ceara', 'atletico', 'avai', 'juventude') #tuplas

print (f'Lista de times do Brasileirão {times}') #saida com os noms dos times

print ('=-' * 30) #separar

print (f'os 5 primeiros colocandos são: {times [:5]}') #os  5 primeiros colocandos

print ('=-' * 30) #separar

print (f'Os 4 ultimos colocandos: {times[-4:]}') #os 4 últimos

print ('=-' * 30) #separar

print (f'Os timas por ordem afabetica {sorted(times)}') #em ordem afabetica

print ('=-' * 30) #separar

print (f'a posicão do Corinthians {times.index("corinthians") + 1}° posicão') #pegar a posição espesificar
