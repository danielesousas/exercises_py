#EXERCÍCIO_17: SEPARANDO DÍGITOS DE UM NÚMERO

num = int(input('Informe um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}...')
print('Unidade: {:.0f}'.format(u))
print('Dezena: {:.0f}'.format(d))
print('Centena: {:.0f}'.format(c))
print('Milhar: {:.0f}'.format(m))