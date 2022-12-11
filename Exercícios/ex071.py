print('='*40)
print('{:^40}'.format('BANCO ANCAP'))
print('='*40)
saq = int(input('Que valor quer sacar? R$'))
c50 = saq//50
c20 = (saq - (50*c50))//20
c10 = (saq - (50*c50) - (20*c20))//10
c1 = (saq - (50*c50) - (20*c20) - 10*c10)//1
print(f'Total de {c50} cédulas de R$50,00')
print(f'Total de {c20} cédulas de R$20,00')
print(f'Total de {c10} cédulas de R$10,00')
print(f'Total de {c1} cédulas de R$1,00')
print('='*40,'\nVolte sempre ao BANCO ANCAP! Tenha um bom dia!')