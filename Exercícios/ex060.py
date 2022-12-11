n = int(input(' Digite um número para calcular seu fatorial: '))
f = 1
print(' Calculando o fatorial de {}! ='.format(n), end='')
while n > 0:
    print(' {} '.format(n), end='')
    print('x' if n != 1 else '= ', end='')
    f *= n
    n -= 1
print('{}'.format(f))
