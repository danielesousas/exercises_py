from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1,8):
    nasc = int(input(f'Qual ano a {pessoa}ª pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Tivemos {totmaior} pessoas MAIORES DE IDADE.')
print(f'Tivemos {totmenor} pessoas MENORES DE IDADE.')
