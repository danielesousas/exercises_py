from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
menu = """
SUAS OPÇÕES:
[0] PEDRA
[1] PAPEL
[2] TESOURA
"""
print(menu)
eu = int(input('Qual a sua escolha? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print(f'Você escolheu {itens[eu]}.')
print(f'O computador escolheu {itens[computador]}.')

if computador == 0:
    if eu == 0:
        print('Empate.')
    elif eu == 1:
        print('Você ganhou.')
    elif eu == 2:
        print('Você perdeu.')
    else: 
        print('Jogada inválida.')
elif computador == 1:
    if eu == 0:
        print('Você perdeu.')
    elif eu == 1:
        print('Empate.')
    elif eu == 2:
        print('Você ganhou.')
    else:
        print('Jogada inválida.')
elif computador == 2:
    if eu == 0:
        print('Você ganhou.')
    elif eu == 1:
        print('Você perdeu.')
    elif eu == 2:
        print('Empate.')
    else:
        print('Jogada inválida.')

