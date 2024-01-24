peso = float (input('Qual seu peso? (Kg) ')) #entra de peso
altura = float (input('Qual a sua altura? (m) '))#entrada de altura
imc = peso / (altura ** 2) #calcular o imc
if imc < 18.5: #se está abaixo do peso
  print (f'vc está ABAIXO do peso, seu imc é {imc:.1f} procure uma nutricionista. ') #saida
elif 18.5 <= imc <=  25: #peso normal
  print(f'Vc está com o peso ideal, seu imc é {imc:.1f} parabéns.') #saida
elif  25 <= imc < 30: #sobrepeso
  print(f'vc está com sobrepeso, seu imc é {imc:.1f} tome cuidado!') #saida
elif imc <= 40: #obesidade
  print (f'vc está com obesidade, seu imc é {imc:.1f} procure uma nutricionista.') #saida 
elif imc >= 40: #acima do peso
 print(f'vc está com obesidade nórbida, seu imc é {imc:.2f} tenha tempo de cuidar da saúde ou vai cuidar da doença.') #saida
 