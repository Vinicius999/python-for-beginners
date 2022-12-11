n1 = int(input(' Digite um número: '))
r = int(input(' Qual a razão? '))
cont = 0
pa = n1
while cont != 10:
    print(' {}'.format(pa), end=',')
    pa += r
    cont += 1
print(' FIM! ')