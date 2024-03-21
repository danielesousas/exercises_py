genero = str(input('Digite seu gênero: [F/M]')).upper().strip()[0]
while genero not in  'MF':
    genero = str(input('Dados inválidos, por favor, informe gênero: ')).upper().strip()[0]
print(f'Gênero {genero} registrado com sucesso!')