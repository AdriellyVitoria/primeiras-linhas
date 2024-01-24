# dados = [] #criar lista
# dados.append('pedro') #add o uma string
# dados.append(25) #add um numero
# #print(dados[0]) #pedro
# #print(dados[1]) #25

# pessoas = []  #criar lista

# dados_1 = [] #criar lista
# dados_1.append('Maria') #add elemento
# dados_1.append(19) #add elemento

# dados_3 = [] #criar lista
# dados_3.append('joao') #add elemento
# dados_3.append(32) #add elemento

# pessoas.append(dados[:]) #add lista entro da lista de pessoas
# pessoas.append(dados_1[:]) #add lista entro da lista de pessoas
# pessoas.append(dados_3[:]) #add lista entro da lista de pessoas

# print (pessoas[0][0])  #chamar elementos da lista
# print (pessoas[1][1]) #chamar elementos da lista
# print (pessoas[2][0]) #chamar elementos da lista
# print(pessoas[1]) #chamar elementos da lista


# teste = [] #criar lista

# teste.append('Gustavo')  #add elemento
# teste.append(40) #add elemento

# galera = list()
# galera.append(teste) #add uma lista dentro da outra
# teste[0] = 'Maria' #trocar os elemento
# teste[1] = 22 #trocar os elemento

# galera.append(teste) #add uma lista dentro da outra

# print (galera) #saida

# galera = [['Joao', 19], ['Ana, 33'], ['Joanquin', 13], ['Maria', 45]] #add varios elementos na lista
# print (galera[2][1]) #chamar elementos

#criar listas
galera = []
dado = []
totmai = totmen = 0
for c in range(0,3): #um for
    dado.append(str ( input ('Nome: '))) #entrad de nomes
    dado.append(int ( input ('Idade: '))) #entrada de idade
    galera.append(dado[:]) #add uma lista dentro da outra *para fazer uma copia [:]
    dado.clear() #limpa a lista
    
for p in galera:
    if p[1] >= 21:
        print (f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print (f'{p[0]} é menor de idade.')
        totmen += 1
        
print (f'Temos {totmai} maiores e {totmai} menores de ideda {galera}')