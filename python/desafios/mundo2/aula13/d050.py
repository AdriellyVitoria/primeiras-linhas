#um programa q leia seis números inteiros e mostre a soma apenas daqueles q forem pares. Se o valor digitado for impar, desconsidedere-o.
soma = contador =  0 #acumulador e contador
for c in range (0, 6): #de 1 a 6
  numero = int (input('Digite um número: '))#entrada
  if numero % 2 == 0: #vai pegar só os numeros pares
    soma += numero #acumular
    contador += 1 #aumento no contador
    
print (f'a soma dos {contador} número pares é {soma}') #saida
