#EXERCÍCIO_05: CONVERSOR DE MOEDAS

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.25

print('Com R${:.2f}, você pode comprar ${:.2f}'.format(real, dolar) )