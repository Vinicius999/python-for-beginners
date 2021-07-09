s = 0
np = 0
for c in range(1, 7):
    n = int(input(' Digite o {}º número: '.format(c)))
    if n % 2 == 0:
        np += 1
        s += n
print(' Foram digitados \033[34m{}\033[m valores pares cujo somatório é igual a \033[1;31m{}\033[m'.format(np, s))
