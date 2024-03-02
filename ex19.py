#EXERCÍCIO_19: PROCURANDO STRING DENTRO DE OUTRA
nome = str(input('Qual o seu nome completo?')).strip()
print('Seu nome tem Lima? {}'.format('lima' in nome.lower()))