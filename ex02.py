#EXERCÍCIO_02: ANTECESSOR E SUCESSOR

n = int(input('Digite um número: '))

print('Analisando o número {}, seu antencessor é {} e seu sucessor é {}'.format(n, (n-1), (n+1)))
#Nesse exercício é melhor usar esse tipo de formatação, sem gerar as variáveis antecessor e sucessor(sem gastar mais memória), pois elas não serão usadas posteriormente
