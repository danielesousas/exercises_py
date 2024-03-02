#EXERCÍCIO_16: ANALISANDO NOME

nome = str(input('Digite seu nome completo: '))

print('Analisando seu nome...')
print(f'Seu nome em letras maiúsculas é {nome.upper()}.')
print(f'Seu nome em letras minúsculas é {nome.lower()}.')
print('Seu nome tem ao todo {} letras.'.format (len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')) )
separa_nome = nome.split()
print(f'Seu primeiro nome é {separa_nome[0]} e tem {len(separa_nome[0])} letras.')