#EXERCÍCIO_22: JOG DA ADIVINHAÇÃO
from random import randint
from time import sleep
computador = randint(0, 5)# faz o programa escolher um número entre 0 e 5
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
num = int(input('Em que número eu pensei? '))
print('LOADING...')
sleep(2)

if num > 5 or num < 0:
    print('Valor inválido.') 
elif num == computador:
    print(f'PARABÉNS! Você acertou! O número escolhido foi {computador}.')
else:
    print(f'Tente novamente! Escolhi {computador}.' )