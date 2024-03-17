#EXERCÍCIO_29: ANALISANDO TRIÂNGULO
print('-'*25)
print('ANALISADOR DE TRIÂNGULOS')
print('-'*25)
lado1 = float(input('1º segmento: '))
lado2 = float(input('2º segmento: '))
lado3 = float(input('3º segmento: '))
if lado1 < lado2 + lado3 and lado2 < lado1 +lado3 and lado3 < lado1 + lado2:
    print('Os segmentos acima PODEM formar um triângulo.')
else:
    print('Os segmentos acima NÃO podem formar um triângulo.')

