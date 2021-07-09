sidade = 0
hmv = 0
mjov = 0
for c in range(1, 5):
    print('-------- {}ª PESSOA --------'.format(c))
    nome = input(' Nome: '.format(c)).strip()
    idade = int(input(' Idade: '.format(c)))
    sexo = input(' Sexo [M/F]: ').strip()
    sidade += idade
    if sexo == 'M' and idade > hmv:
        hmv = idade
        hmvnome = nome
    elif sexo == 'F' and idade < 20:
        mjov = mjov + 1
print('-'*30)
print(' Média de idade: {}'.format(sidade/4))
print(' O homem mais velhor é {}, com {} anos.'.format(hmvnome, hmv))
print(' Melheres abaixo dos 20 anos: {}'.format(mjov))

