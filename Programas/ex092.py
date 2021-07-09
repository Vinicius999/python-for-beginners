from datetime import date
pessoa = dict()

pessoa['nome'] = input('Nome: ')
nasc = int(input('Ano de nascimento: '))
pessoa['idade'] = date.today().year - nasc
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de cadastro: '))
    pessoa['salario'] = float(input('Salário: R$ '))
    pessoa['aposentadoria'] = pessoa['idade'] + (35 - (date.today().year - pessoa['contratação']))
print('-='*20)
print(f'{pessoa}')
for k, v in pessoa.items():
    print(f'{k} tem o valor de {v}')
