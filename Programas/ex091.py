from random import randint
from time import sleep
from operator import itemgetter
jogo = dict()

for j in range(1, 5):
    jogo[f'jogador{j}'] = randint(1, 6)
print('Jogadores sorteados: ')
ranking = list()

for k, v in jogo.items():
    print(f'   O {k} tirou {v}')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(' == Ranking dos Jogadores ==')

for k, v in enumerate(ranking):
    print(f'{k+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
