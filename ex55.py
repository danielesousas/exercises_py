from random import randint
from time import sleep
pc = randint(0, 10)
palpite = 0
print('Hello, sou o seu computador...Pensei em um número em um número entre 0 e 10')
sleep(2)
print('Será que você consegue acertar? ')
sleep(1)
acertou = False
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpite += 1
    if jogador == pc:
        acertou = True
    
    else:
        if jogador < pc:
            print('Mais... Tente novamente...')
        elif jogador > pc:
            print('Menos... Tente novamente')
print(f'Pensei no número {pc}. Você acertou com {palpite} tentativas.')