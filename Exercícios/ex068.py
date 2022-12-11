from random import randint
p_jog = ' '
acertos = 0
while True:
    print('-=' * 20)
    njog = int(input(' Digite um valor: '))
    while p_jog not in 'PpIi':
        p_jog = input(' Par ou Ímpar? [P/I] ').upper().strip()[0]
    print('-'*40)
    if p_jog == 'P':
        p_jog = 'PAR'
    else:
        p_jog = 'ÍMPAR'
    ncomp = randint(0, 10)
    if (ncomp + njog) % 2 == 0:
        result = 'PAR'
    else:
        result = 'ÍMPAR'
    print(f' Você jogou {njog} e o computador jogou {ncomp}. Total deu {ncomp+njog} que é {result}')
    if result != p_jog:
        print(' Você \033[31mPERDEU!\033[m')
        break
    else:
        print(' Você \033[34mVENCEU!\033[m\n Vamos jogar novamente...')
        acertos += 1
print('-='*20)
print(f' GAME OVER! Você venceu {acertos} vezes.')

