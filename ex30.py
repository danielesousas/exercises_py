#EXERCÍCIO_30: APROVANDO EMPRÉSTIMO
valor = float(input('Valor da casa: R$'))
salario = float(input('Qual o salário do comprador? R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = valor /(anos * 12)


if prestacao > (salario * 0.3):
    print('Empréstimo NEGADO!')
else:
    print(f'APROVADO! O valor da mensalidade será de R${prestacao:.2f}.')
