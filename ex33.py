#EXERCÍCIO_33: ALISTAMENTO MILITAR
from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}.')
if idade == 18:
    print('E precisa se alistar IMEDIATAMENTE.')
elif idade < 18:
    print(f'Faltam {18 - idade} anos para se alistar.')
else:
    print(f'Seu alistamento foi a {idade - 18} atrás.')