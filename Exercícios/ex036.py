print('{:=^40}'.format('EMPRÉSTIMO'))
casa = float(input(' Valor da casa desejada: R$'))
sal = float(input(' Seu salário: R$'))
ano = int(input(' Quantos anos de financiamento? '))
prest = casa/(ano*12)
if prest > sal*0.3:
    print(' O empréstimo foi \033[1;31mNEGADO\033[033m')
else:
    print(' O empréstimo foi \033[1;34mCONSEDIDO\033[m.')
