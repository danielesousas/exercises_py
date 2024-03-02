#EXERCÍCIO_10: ALUGUEL DE CARROS

km = float(input('Quantidade de quilômetros percorridos: '))
dias = int(input('Dias alugado: '))
preco_dia = dias * 60
preco_km = km * 0.15
preco_total = preco_km + preco_dia

print(f'O carro alugado por {dias} dias e percorrendo {km} km, custará o total de R$ {preco_total:.2f}.')