m_barato = ' '
ac_1000 = tot_preco = c = 0
while True:
    cont = '!'
    prod = input(' Nome do produto: ')
    preco = float(input(' Preço: R$'))
    tot_preco += preco
    c += 1
    if preco > 1000:
        ac_1000 += 1
    if c == 1:
        pm_barato = preco
        m_barato = prod
    if preco < pm_barato:
        m_barato = prod
    while cont not in 'SsNs':
        cont = input(' Deseja continuar? [S/N]').upper().strip()
    if cont[0] == 'N':
        break
print('{:-^35}'.format(' FIM DO PROGRAMA '))
print(f'Preço total: R${tot_preco:.2f}\n Temos {ac_1000} produtos acima de R$1000,00\nProduto mais barato: {m_barato:.2f} ,R${pm_barato}')



