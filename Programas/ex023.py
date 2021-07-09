n = input(' Digite um número entre 0 e 9999: ')
lista = ('{:>4}'.format(n))
print(' Unidades: {}'.format(lista[3].replace(' ', '0')))
print(' Dezenas: {}'.format(lista[2].replace(' ', '0')))
print(' Centenas: {}'.format(lista[1].replace(' ', '0')))
print(' Milhares: {}'.format(lista[0].replace(' ', '0')))

