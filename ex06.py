#EXERCÍCIO_06: PINTANDO PAREDE 

largura = float(input('Qual a largura da parede, em metros? '))
altura = float(input('Qual a altura da parede, em metros? '))
area = largura * altura
litros = area / 2.5

print('Com uma área de {}m², você precisará de {} litros de tinta.'.format(area, litros))