from random import randint
from time import sleep


def sorteia(num):
    print('Sorteando os valores da lista: ',end='')
    for c in range(0, 5):
        n = randint(0, 10)
        sleep(0.3)
        print(f'{n}', end=' ')
        num.append(n)
    print('PRONTO!')


def somaPar(num):
    spar = 0
    for n in num:
        if n % 2 == 0:
            spar += n
    print(f'Somando os valores pares de {num}, temos {spar}')


números = list()
sorteia(números)
somaPar(números)
