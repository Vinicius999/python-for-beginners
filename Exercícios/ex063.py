n1 = 0
n2 = 1
cont = int(input(' Quantos termos da sequência de Fibonacci deseja ver? '))
while cont > 0:
    print(' {}'.format(n1), end=',')
    n1 = n1+n2
    cont -= 1
    if cont > 0:
        print(' {}'.format(n2), end=',')
        n2 = n1 + n2
    cont -= 1
print(' FIM!')
