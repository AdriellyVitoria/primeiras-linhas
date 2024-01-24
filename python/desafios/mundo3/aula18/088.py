from random import randint
print ('MEGA SENA')
giros = 0
jogo = int (input ('Quantos jogos voce quer que eu sorteie? '))
print (F'=-=-=- SORTEANDO {jogo} JOGOS -=-=-=')
while giros < jogo:
    giros += 1  
    lista = []
    while len(lista) < 6:     
        numero = int (randint(0, 60))
        if numero not in lista:
            lista.append(numero)
    print (f' jogo {giros}: {lista}')