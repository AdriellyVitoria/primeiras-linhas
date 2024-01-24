lista = []
expressao = input ('Digite uma expressão: ')

for simb in expressao:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
            
if len(lista)== 0:
    print ('sua expresão está correta')
else:
    print ('Sua expressão está errada')