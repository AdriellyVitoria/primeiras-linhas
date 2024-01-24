nota1, nota2 = map (float, input ('Suas notas: ').split()) #recebe notas
soma = (nota1 + nota2) / 2 #media
if soma < 5: #se for menor que 5
 print(f'vc foi reprovado porque sua nota {soma:.1f} e está abaixo de 5.0') #saida
elif 7 > soma >= 5: #se for entre 7 e 5
  print(f'vc ficou em recuperação, pois sua nota foi {soma:.1f}') #saida
elif soma >= 7.0 and soma < 10: # se for acima de 7
  print (f'Parabéns vc foi aprovando, sua nota foi {soma:.1f}') #saida
elif soma == 10: #se for 10
  print (f'Parabéns, sua nota foi excelente, {soma:.1f}') #saida
