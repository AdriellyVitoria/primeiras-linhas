lanche = ('hamburgues', 'suco', 'pizza', 'pudim', 'batata frita')
(lanche[1])

# # print (sorted (lanche)) #organizar 

# for cont in range (0, len(lanche)): #se precisa da posiçaõ de usar len 
#   print (lanche[cont])

for pos, comida in enumerate (lanche): #ou o enumerate
 print (f'Eu vou comer {comida} na posicão {pos}')

# lanche = ('hamburgues', 'suco', 'pizza', 'pudim')
# for comida in lanche: #se não precisa da posição
#   print (f'Eu vou comer {comida}')
# print ('Comir muito')



# a = (2, 5, 4)
# b =  (5, 8, 1, 2)
# c = a + b #vai junta os valores
# #print (c.count(5)) # para verificar quantas numero igual aparece 
# print (c)
# print (c.index (8)) #mostra em q possição está o numero q está em parentes, pode descolar tbm

#posso tem dados diferente dentro da tupla
#a tupla é inutavel, mas pode apagar a tupla inteiro com del ()


