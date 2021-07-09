n1 = int(input(' Valor inicial da PA: '))
r = int(input(' Razão da PA: '))
for c in range(n1, r*10, r):
    print(' -> {}'.format(c), end='')
print(' >>FIM! ')