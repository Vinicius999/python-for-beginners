n = int(input(' Digite um número para saber se ele é primo: '))
p = 0
for c in range(1, n+1):
    if n%c == 0:
       p = p + 1
print('> {} é PRIMO!'.format(n) if p == 2 else '> {} NÃO é PRIMO!'.format(n))
