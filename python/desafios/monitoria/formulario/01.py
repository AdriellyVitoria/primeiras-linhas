#Descreva o comportamento do programa se a entrada do usuário for igual a:
# a) 0
# b) 4.6
# c) Cinco

categoria = int(input("Digite a categoria do produto: "))

if categoria == 1:
    preco = 10

else:
    if categoria == 2:
        preco = 18
    else:
        if categoria == 3:
            preco = 23
        else:
            if categoria == 4:
                preco = 26
            else:
                if categoria == 5:
                    preco = 31

print(f"O preço do produto é: R${preÇo:6.2f}")  


