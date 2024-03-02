#EXERCÍCIO-20: 1ª E ÚLTIMA OCORRÊNCIA DE UMA STRING
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aperece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A, apareceu na posição {}.'.format(frase.find('A')+1))
print('A última leta A apreceu na posição {}.'.format(frase.rfind('A')+1))