valor = int (input ('Digite um número: '))
if valor <= 100:
    # 5% de taxa
    taxa = valor * 0.05
else:
    # 10% de taxa
    taxa = valor * 0.1

print(f'A taxa a ser paga é R$ {taxa:.2f}')
