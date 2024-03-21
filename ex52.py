maior = 0
menor = 999999
for pessoa in range(1, 6):
    peso = float(input(f'Digite o peso da {pessoa}ª pessoa: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O maior peso lido é {maior:.2f}Kg.')
print(f'O menor peso lido é {menor:.2f}Kg.')
