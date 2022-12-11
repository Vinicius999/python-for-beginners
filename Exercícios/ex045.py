from random import choice
from time import sleep
co = ['PEDRA', 'PAPEL', 'TESOURA']
co = choice(co)
print('{:=^40}'.format('JOKENPÔ'))
esc = int(input('[1]PEDRA       [2]PAPEL       [3]TESOURA\n >> Escolha: '))
if esc == 1:
    jo = 'PEDRA'
elif esc == 2:
    jo = 'PAPEL'
elif esc == 3:
    jo = 'TESOURA'
else:
    print(' Jogada Inválida!')
print('   JO', end=' ')
sleep(1)
print('   KEN', end=' ')
sleep(1)
print('   PO !')
sleep(1)
print('-'*40)
print('    Você escolheu \033[1;31m{}\033[m \n    O computador escolheu \033[1;34m{}\033[m'.format(jo, co))
print('-'*40)
if co == 'PEDRA' and esc == 3 or co == 'PAPEL' and esc == 1 or co == 'TESOURA' and esc == 2:
    print('       >> COMPUTADOR VENCE <<')
elif co == 'PEDRA' and esc == 2 or co == 'PAPEL' and esc == 3 or co == 'TESOURA' and esc == 1:
    print('        >> JOGADOR VENCE <<')
else:
    print('            >> EMPATE <<')