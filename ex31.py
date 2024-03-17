#EXERCÍCIO_31:CONVERSOR DE BASES NUMÉRICAS

print('-'*30)
print('CONVERSOR DE BASES NUMÉRICAS')
print('-'*30)
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para fazer a conversão:
      [1] converter para BINÁRIO
      [2] converter para OCTAL
      [3] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:#usando funções nativas do python(bin(), oct() e hex())
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}.')#[2:]ler a string apartir do idex 2 pra frente
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}.')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}.')
else:
    print('Valor inválido')