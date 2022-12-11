s = 0
p = ''
cont = 0
while p != 'S':
    n = int(input('Digite um número: '))
    s += n
    cont += 1
    if cont == 1:
        maior = menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    p = input(' Deseja parar? {S/N} ').upper()
print('\n Média dos valores: {:.1f}\n Maior valor: {}\n Menor valor: {}'.format(s/cont, maior, menor))

