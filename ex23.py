#EXERCÍCIO_23: RADAR DE VELOCIDADE
print('-' *10 + 'RADAR DE VELOCIDADE' + '-' *10)
print(' ')
vel = float(input('Qual a velocidade do carro? '))
limite = 80
multa = (vel - limite) * 5
if vel > limite:
    print('MULTADO! Você excedeu o limite permitido, que é de 80Km/h.')
    print(f'Terá que pagar valor R${multa:.2f}.')
print('Tenha um bom dia! Dirija com segurança!')