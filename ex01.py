#EXERCÍCIO_01: ANALISANDO UMA VARIÁVEL

a = input('Digite algo: ')

print(f'O tipo primitivo é? {type(a)}')
print(f'Só tem espaços? {a.isspace()}')
print(f'É numérico? {a.isnumeric()}')
print(f'É alfabético? {a.isalpha()}')
print('É alfanumérico? ', a.isalnum())
print(f'Está em maiúsculas? {a.isupper()}')
print(f'Está minúscula? {a.islower()}')
print(f'Está capitalizada? {a.istitle()}')