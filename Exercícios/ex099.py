from time import sleep


def maior(* num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    for n in num:
        print(f'{n}', end=' ')
        sleep(0.3)
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor foi ', end='')
    if len(num) == 0:
        print(f'{len(num)}.')
    else:
        print(f'{max(num)}.')


maior(7, 5, 9, 12)
maior(0, 2, 4, 5, 1)
maior(1, 3, 1, 0, 5, 5)
maior(1, 2)
maior(6)
maior()
