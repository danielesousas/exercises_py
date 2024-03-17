#EXERCÍCIO_27: AUMENTOS MÚLTIPLOS
salario = float(input('Qual o salário do funcionário? '))
if salario <= 1250:
    novo = salario + (salario * 0.15)
    print(f'O funcionário terá o novo salário de R${novo:.2f}.')
else:
    novo= salario + (salario * .1)
    print(f'O funcionário terá o novo salário de R${novo:.2f}.')