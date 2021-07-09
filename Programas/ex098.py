from time import sleep


def contador(inicio, fim, passo):
    print('-=' * 20)
    print(f'Contágem de {inicio} até {fim} de {passo} em {passo}')
    if inicio > fim:
        if passo > 0:
            passo = -passo
        elif passo == 0:
            passo = -1
        fim += passo
    if inicio < fim:
        if passo < 0:
            passo = -passo
        elif passo == 0:
            passo = 1
        fim += passo
    for n in range(inicio, fim, passo):
        print(f'{n}', end=' ')
        sleep(0.4)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
