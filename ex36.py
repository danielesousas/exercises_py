#EXERCÍCIO_36: ANALISANDO TRIÂNGULO V2.0
print('-'*25)
print('ANALISADOR DE TRIÂNGULOS')
print('-'*25)
lado1 = float(input('1º segmento: '))
lado2 = float(input('2º segmento: '))
lado3 = float(input('3º segmento: '))
if lado1 < lado2 + lado3 and lado2 < lado1 +lado3 and lado3 < lado1 + lado2:
    print('Os segmentos acima PODEM formar um triângulo.')
    if lado1 == lado2 and lado1 == lado3:
        print('E esse triângulo é EQUILÁTERO.')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('E esse triângulo é ISÓSCELES.')
    else:
        print('E esse triãngulo é ESCALENO.')
else:
    print('Os segmentos acima NÃO podem formar um triângulo.')

