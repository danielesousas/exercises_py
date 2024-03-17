#EXERCÍCIO_25: CUSTO DE VIAGEM
distancia = float(input('Qual a distância da sua viagem, em km? '))
print('Você está prestes a começar uma viagem de {}km.'.format(distancia))
"""if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45"""
preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45#operador ternario
print(f'E o preço da sua passagem será de R${preco:.2f}.')
