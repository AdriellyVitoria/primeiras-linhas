nome = input ('Digite o nome do arquivo: ') #pegar o nome do arquivo já criando

arquivo = open(nome,'r') #vai ler o arquivo

for linha in arquivo: #pecorre as linhas do arquivo desejando pelo o usuario
    print (linha, end='') #imprimir a linha do arquivo

arquivo.close() #fecha o arquivo
