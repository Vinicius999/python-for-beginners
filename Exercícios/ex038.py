n1 = int(input(' 1º número: '))
n2 = int(input(' 2º número: '))
if n1 > n2:
    print(' {} é maior'.format(n1))
elif n2 > n1:
    print(' {} é maior'.format(n2))
else:
    print(' Os dois valores são idênticos. Não há maior.')
