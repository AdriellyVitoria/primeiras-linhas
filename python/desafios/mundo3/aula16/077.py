
palavras = ('Amor', 'beijos', 'Lula', 'Castiel')
for letras in (palavras):
  print (f'\nNa palavra {letras.upper()} temos ', end='')
  for p in (letras):
    if p.lower() in 'aeiou':
        print (p, end=' ')