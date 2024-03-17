print('{:=^40}'.format('SHOPPING SHOW'))
valor = float(input('Preço das Compras: R$'))
menu = """
FORMAS DE PAGAMENTO
[1] à vista em dinheiro
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
"""

print(menu)
m = int(input("Qual a opção? "))

if m == 1:
    preco = valor - (valor * 0.1)
    print(f'Sua compra, paga em dinheiro, à vista, será no total de R${preco:.2f}')
elif m == 2:
    preco = valor - (valor * 0.05)
    print(f"Sua compra, paga à vista, no cartão, será de R${preco:.2f}. ")
elif m == 3:
    preco = valor
    print(f'Sua compra, paga em 2x no cartão, será de R${valor:.2f}')
elif m == 4:
    preco = valor + (valor * 0.2)
    parcelas = int(input('Quantas parcelas: '))
    if parcelas >=3:
        print(f"Com {parcelas} parcelas, o valor será de R${preco:.2f}")
    else:
        print('Número de parcelas inválido.')
else:
    print('Modo de pagamento inválido.')
