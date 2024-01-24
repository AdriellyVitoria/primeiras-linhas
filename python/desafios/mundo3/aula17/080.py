lista = [] #criar lista

for i in range (5): #rodar 5 veses
    numero = int (input ('Digite um numero: ')) #entrada

    if i == 0 or numero > lista[-1]:
        print ('Adicionado ao final da lista...') #saida
        lista.append(numero)
        
    else:
       pos = 0
       while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                print (f'Adicionado na posição {pos} da lista')
                break
            pos += 1

print ('-=' * 30)
print (f'Os valores digitandos em ordem foram {lista}')
