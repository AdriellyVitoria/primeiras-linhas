quantos_testes = int (input ('Digite quantas notas vc deseja add: ')) #vai receber o numero de quantas notas vai ser add

errou_mais = 0 #para pegar os erros maiores

for i in range (1, quantos_testes + 1): #vai girar até o numero digitando acima
    erro = 0 #contandor e ao mesmo tempo vai zera
    prova = input('Digite os acertos dos alunos: ') #digitar as notas

  
    for j in range(len(prova)): #vai pegar os elementos separadamente
        if prova[j] == 'f': #se for igual a f
            erro += 1 #vai acumular o erro

    if erro > errou_mais: #vai pegar o aluno q errou mais
        errou_mais = erro #vai salvar quantos erros
        posição = i #pegar a posição do aluno q errou mais

print(f'O aluno {posição} errou {errou_mais} teste(s).') #saida do aluno e quantos errou
