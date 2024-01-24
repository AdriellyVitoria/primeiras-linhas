x1, y1 = map (float, input().split())
x2, y2 = map (float, input().split())

# x1 = float(x1)
# y1 = float(y1)
# x2 = float(x2)
# y2 = float(y2)

distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(f'{distancia:.4f}')

# Exemplo de Entrada	Exemplo de Saída
# 1.0 7.0
# 5.0 9.0
# 4.4721
