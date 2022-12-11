def metade(n, f=False):
    return n / 2 if not f else moeda(n)


def dobro(n, f=False):
    return n * 2 if not f else moeda(n)


def aumentar(n, p=0, f=False):
    return n + (n/100) * p if not f else moeda(n)


def diminuir(n, p=0, f=False):
    return n - (n/100) * p if not f else moeda(n)


def moeda(p=0, moeda='R$'):
    v = int(p)
    return f'{moeda}{v:.2f}'.replace('.', ',')


def resumo(m, aum, red):
    print('-' * 30)
    print(f'{str("RESUMO DO VALOR"):^30}')
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(m)}')
    print(f'Dobro do preço: \t{dobro(m, True)}')
    print(f'Metade do preço: \t{metade(m, True)}')
    print(f'{aum}% de aumento: \t{aumentar(m, aum, True)}')
    print(f'{red}% de redução: \t{diminuir(m, red, True)}')
    print('-' * 30)
