km = float(input(' Quantos quilômetros percorridos: '))
dias = int(input(' O aluguel durou quantos dias: '))
alu = (dias * 60) + (km * 0.15)
print(' O valor a ser pago é R${:.2f}'.format(alu))

