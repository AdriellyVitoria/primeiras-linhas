pessoas = []
nomeMaior = []
nomeMenor = []
maior = 0

while True:
    dados = []
  
    dados.append(str (input ('Digite seu nome: ')))
    dados.append(int (input ('Digite o seu peso: ')))
    pessoas.append(dados[:])
    continuar = input ('Quer continuar: [S/N] ').upper()
    if continuar == 'N':
        break

menor = pessoas[0][1]
maior = pessoas[0][1]


for p in pessoas:
    if p[1] >= maior:
        maior = p[1]
        nomeMaior.append(p[0])

    if p[1] <= menor:
        menor = p[1]
        nomeMenor.append(p[0])

print (f'Temos {len(pessoas)} cadatranda\nO maior peso foi de {nomeMaior} com {maior}Kg\nO menor peso é de {nomeMenor} com {menor}Kg')
