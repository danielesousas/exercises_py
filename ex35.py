#EXERCÍCIO_35: CLASSIFIANDO ATLETAS
from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
if idade <= 10:
    print(f'Esse atleta tem {idade} anos e é classificado como MIRIM.')
elif idade <= 14:
    print(f'Esse atleta tem {idade} anos e é classificado como INFANTIL.')
elif idade <= 19:
    print(f'Esse atleta tem {idade} anos e é classificado como JÚNIOR.')
elif idade <= 25:
    print(f'Esse atleta tem {idade} anos e é classificado como SÊNIOR.')
else:
    print(f'Esse atleta tem {idade} anos e é clasificado como MASTER. ')