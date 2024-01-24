print('-='*20)
print('Analisador de Triângulos')
print ('-='*20)
r1, r2, r3 = map (float, input ('segmentos: ').split ())
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
  print ('Os segmentos acima PODEM FORMAR um TRIÂNGULO. ') 
  if r1 == r2 == r3:
    print ('EQUILÁTERO.')
  elif r1 != r2 != r3 != r1:
    print('ESCALENO.')
  else:
    print ('ISÓSCELES')
else:
  print('Os segmentos acima NÃO PODEM FORMAR TRIÂNGULO!')
