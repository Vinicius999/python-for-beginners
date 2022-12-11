def área(l, c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é {a:.1f}m².')


print(' Controle de Terrenos')
print('-' * 25)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
área(larg, comp)