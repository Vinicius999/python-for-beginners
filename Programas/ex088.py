from random import randint
from time import sleep

mega = list()

print('-'*40)
print('{:^40}'.format('JOGO NA MEGA SENA'))
print('-'*40)
c = int(input('Quantos jogos voçê quer que eu sorteie? '))

for n in range(0, c):
    mega.append(list())
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in mega[n]:
            mega[n].append(num)
            cont += 1
        if cont == 6:
            mega[n].sort()
            break

print(f'=-=-=-=-  SORTENADO {c} jogos  -=-=-=-=')
for n, cont in enumerate(mega):
    print(f'Jogo {n+1}: {cont}')
    sleep(1)
print(f'-=-=-=-=-=-= < BOA SORTE > -=-=-=-=-=-=')