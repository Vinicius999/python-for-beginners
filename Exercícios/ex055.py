maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(' Peso da {}ª pessoa (kg): '.format(c)))
    if c == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('> Maior peso lido: {}Kg\n> Menor peso lido: {}Kg'.format(maior, menor))
