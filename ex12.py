#EXERCÍCIO_12: CATETOS E HIPOTENUSA
from math import hypot
c1 = float(input('Comprimento do cateto oposto: '))
c2 = float(input('Comprimento do cateto adjacente: '))
h = hypot(c1, c2)

print(f'Com o cateto oposto medindo {c1} e o cateto adjacente medindo {c2}, a hipotenusa medirá {h:.2f}.')

"""
c1 = float(input('Comprimento do cateto oposto: '))
c2 = float(input('Comprimento do cateto adjacente: '))
h= ((c1*c1 + c2*c2) ** (1/2))

print(f'Com o cateto oposto medindo {c1} e o cateto adjacente medindo {c2}, a hipotenusa medirá {h:.2f}.')"""