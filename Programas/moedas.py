def metade(n, f=False):
    if f:
        return f'R${int(n / 2)},00'
    else:
        return n / 2


def dobro(n, f=False):
    if f:
        return f'R${int(n * 2)},00'
    else:
        return n * 2


def aumentar(n, p=0, f=False):
    if f:
        return f'R${int(n + (n / 100) * p)},00'
    else:
        return n + (n/100) * p


def diminuir(n, p=0, f=False):
    if f:
        return f'R${int(n - (n / 100) * p)},00'
    else:
        return n - (n/100) * p


def moeda(m):
    v = int(m)
    return f'R${v},00'


def resumo(m, aum, red):
    print('-' * 30)
    print(f'{str("RESUMO DO VALOR"):^30}')
    print('-' * 30)
    print(f'{str("Preço analisado:"):<20}{moeda(m)}')
    print(f'{str("Dobro do preço:"):<20}{dobro(m, True)}')
    print(f'{str("Metade do preço:"):<20}{metade(m, True)}')
    print(f'{aum}%{str(" de aumento:"):<17}{aumentar(m, aum, True)}')
    print(f'{red}%{str(" de redução:"):<17}{diminuir(m, red, True)}')
    print('-' * 30)
