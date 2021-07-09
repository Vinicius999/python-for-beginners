def fatorial(n, show=False):
    """
    -> Calcula o fatorial de m número
    :param n: O número a ser calculado
    :param show: (opcional) Mostra ou não a conta
    :return: O valor do Fatorial de um número n
    """
    fat = 1
    print('-' * 30)
    for x in range(n, 0, -1):
        fat *= x
        if show:
            print(f'{x}', end=' ')
            if x > 1:
                print(f'x ', end='')
            else:
                print('=', end=' ')
    return fat


print(fatorial(5, True))
