#EXERÇICIO_20: 1º E ÚLTIMO NOME DE UMA PESSOA
nome = str(input('Qual seu nome completo? ')).strip()
n = nome.split()
print('Nice to meet you!')
print('Seu primeiro nome é {}.'.format(n[0]))
print('Seu último nome é {}.'.format(n[len(n)-1]))
