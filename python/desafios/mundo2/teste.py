frase = input("Digite uma frase: ").lower()
caractere = input("Digite um caractere: ").lower()
posicoes = []

for i in range(len(frase)):
    if frase[i] == caractere:
        posicoes.append(i)

if posicoes:
    print(f"O caractere '{caractere}' aparece nas posições: {posicoes}")
else:
    print(f"O caractere '{caractere}' não foi encontrado na frase.")
        
        