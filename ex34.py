#EXERCÍCIO_34: MÉDIA
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if media > 7:
    print('Aluno aprovado! PARABÉNS!')
elif media >= 5 and media < 6.9:
    print('Aluno de RECUPERAÇÃO!')
else:
    print('Aluno REPROVADO! ')