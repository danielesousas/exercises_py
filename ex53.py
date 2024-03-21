somaidade = 0
mediaidade = 0
maioridadehomem = ''
nomemaisvelho = ''
totmulher20 = 0
for x in range(1, 5):
    print('-'*5 + f' {x}ª PESSOA' + '-'*5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]')).upper()
    somaidade += idade 
    if x == 1 and sexo in 'M':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'F' and idade <= 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade:.0f} anos.')
print(f'O homem mais velho tem {maioridadehomem:.0f} anos e se chama {nomemaisvelho}.')
print(f'Ao todo são {totmulher20} mulher(es) com menos de 20 anos.')