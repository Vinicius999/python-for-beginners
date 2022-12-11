s = float(input(' Valor do salário: R$'))
if s > 1250:
    print(' Aumento de 10%: R${:.2f}\n Salário final: R${:.2f}'.format(s*0.1, (s*0.1)+s))
else:
    print(' Aumento de 15%: R${:.2f}\n Salário final: R${:.2f}'.format(s*0.15, (s*0.15)+s))
