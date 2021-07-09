adultos = h = m_jov = 0
while True:
    sexo = cont = ' '
    print(f'------------------------------\n    CADASTRE UMA PESSOA\n------------------------------')
    idade = int(input('Idade: '))
    while sexo not in 'MmFf':
        sexo = input('Sexo: ').upper().strip()
    if idade >= 18:
        adultos += 1
    if sexo in 'Mm':
        h += 1
    if sexo in 'Ff' and idade < 20:
        m_jov += 1
    while cont not in 'SsNn':
        cont = input(' Deseja continuar [S/N]? ').upper().strip()
    if cont == 'N':
        break
print('========= FIM DO PROGRAMA =========')
print(f'Total de maiores de 18 anos: {adultos}')
print(f'Total de homens: {h}')
print(f'Total de mulheres abaixo dos 20 anos: {m_jov}')