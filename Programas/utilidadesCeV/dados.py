def leiaDinheiro(m):
    while True:
        d = input(m)
        if d.replace(',', '0').isnumeric() or d.replace('.', '0').isnumeric():
            d = d.replace(',', '.')
            return float(d)
            break
        print(f'\033[31mERRO! ¨{d}¨ é um preço inválido.\033[m')


'''p = leiaDinheiro('Digite um preço: R$')
print(p)'''
