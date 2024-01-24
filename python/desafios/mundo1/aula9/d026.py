frase = str (input('diga uma frase: ')).upper().strip()
print (f'na frase {frase} apareceu {frase.count ("A")} vezes a letra A')
print (f' A letra A apareceu pela a primeira vez em:  {frase.find("A")+1}')
print (f'A letra A aparecer pela a última vez em {frase.rfind("A")+1}')