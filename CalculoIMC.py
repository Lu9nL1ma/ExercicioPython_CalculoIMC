# Criando uma calculadora de Indice de Massa Corporal
# Utilizando condicionais compostas


peso_kg = float(input("Insira seu peso atual (Kg): "))
altura_M = float(input("Insira sua altura (m): "))
calculo_imc = peso_kg / (altura_M ** 2)

print("O seu IMC é de {:.1f}".format(calculo_imc))

if calculo_imc < 18.5:
  print("Você está abaixo do peso ideal!")

elif calculo_imc >= 18.6 and calculo_imc < 24.9:
  print("Parabéns, você esta no peso ideal!!")

elif calculo_imc >= 25.0 and calculo_imc < 29.9:
  print("Você está levemente acima do peso...")

elif calculo_imc >= 30.0 and calculo_imc < 34.9:
  print("Cuidado, você está na obesidade de Grau I!")

elif calculo_imc >= 35.0 and calculo_imc < 39.9:
  print("Você está na Obesidade de Grau II (Severa)!!")

else:
  print("Obesidade de Grau III (Mórbida), consulte seu médico")
