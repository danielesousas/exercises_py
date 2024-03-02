#EXERCÍCIO_07: CALCULANDO DESCONTOS

preco = float(input('Qual o valor do produto? '))
desconto = float(input('Qual o valor do desconto, em porcentagem? '))
porcentagem = desconto / 100
valor_final = preco - (preco * porcentagem)

print(f'O valor final do produto será : R${valor_final:.2f}')