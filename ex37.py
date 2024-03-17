#EXERCÍCIO_37: IMC
peso = float(input('Qual o seu peso? (Kg)'))
altura = float(input('Qual a sua altura? (m)'))
imc = peso / (altura*altura)
print(f'O IMC dessa pessoa é {imc:.2f}')


if imc < 18.5:
    print('Está ABAIXO DO PESO.')
elif 18.5 <= imc < 25:
    print('Está com o PESO NORMAL.')
elif 25 <= imc < 30:
    print('Está em SOBREPESO.')
else:
    print('Está com OBESIDADE.')
