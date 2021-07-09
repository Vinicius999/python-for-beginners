from random import randint
jog = int(input(' Estou pensando em um número...\n Consegue adivinhar qual? '))
comp = randint(0, 10)
cont = 1
while jog != comp:
    cont += 1
    if jog > comp:
        jog = int(input('Menos... Tente mais uma vez.\n Qual seu palpite? '))
    else:
        jog = int(input('Mais... Tente mais uma vez.\n Qual seu palpite? '))
print(' Acertou com {} tentativas. PARABÉNS!'.format(cont))
