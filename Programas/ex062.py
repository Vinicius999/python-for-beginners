pa = int(input(' Digite um número: '))
r = int(input(' Razão: '))
cont = 0
e = ''
total = 10
while e != 0:
    while cont < total:
        print('> {}'.format(pa), end=' ')
        pa += r
        cont += 1
    e = int(input('\n Deseja ver mais quantos termos da PA? '))
    total += e
print(' Foram mostrados {} temos da PA'.format(total))