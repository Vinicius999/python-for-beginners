valor = float(input(' Preço do produto: R$'))
print('-'*40)
print(' [1] À vista dinheiro/cheque: 10% de desconto')
print(' [2] À vista no catão de crédito: 5% de desconto')
print(' [3] Em até 2x no cartão de crédito: preço normal')
print(' [4] 3 ou mais vezes no cartão de crédito: 20% de juros')
cp = int(input('>> Condição de pagamento: '))
if cp == 1:
    print(' Valor final: R${:.2f}'.format(valor*0.9))
elif cp == 2:
    print(' Valor final: R${:.2f}'.format(valor*0.95))
elif cp == 3:
    print(' 2 parcelas de R${:.2f}\n Valor final: R${:.2f}'.format(valor/2, valor))
elif cp == 4:
    p = (int(input(' Quantas parcelas? ')))
    print(' {}x de R${:.2f}, totalizando R${:.2f} '.format(p, valor*1.2/p ,valor*1.2))
else:
    print(' Opção inválida de pagamento.')