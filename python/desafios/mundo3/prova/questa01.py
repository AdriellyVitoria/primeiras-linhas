def ler_lista(lista): #a função ler lista
    i = 0 #contando

    #o laço com enquanto, pois, com for remover elementos deixaria o i maior q a lista

    while i < len(lista): #enquanto o i for menor q os elementos da lista

        if type(lista[i]) == str: #verificar se e string
            lista.pop(i) #para remover a string da lista
        else: #só incrementa se não remover o item, caso contrario um item seria pulado
            i += 1 #incremento 

    return lista #retonar a lista
    
             
lista = [1, 2, 2, '4', '5', 6, 9, 'b', 't'] #passar como paramentro uma lista já existente 

print(ler_lista(lista)) #chamar a fução como o paramentro lista