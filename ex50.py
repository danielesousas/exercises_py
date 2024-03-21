frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()#separando as palvras
junto = ''.join(palavras)#juntando as palavras com um sem espaco(tenmte: junto = *.join(palavras))
#inverso = ''#inverso começa vazio
inverso = junto[::-1]
"""for letra in range(len(junto)-1, -1, -1):
    inverso+= junto[letra]"""
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto:
    print('Temos um palídromo!')
else:
    print('Não temos um palídromo.')