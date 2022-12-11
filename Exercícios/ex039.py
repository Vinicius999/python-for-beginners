from datetime import date
sexo = input(' [F] para mulher\n [M] para homem\n Seu sexo: ').upper()
if sexo == 'M':
    nasc = int(input(' Ano de Nascimento: '))
    idade = date.today().year - nasc
    if idade < 18:
        print(' Faltam {} ano(s) para se alistar ao serviço militar.'.format(17-idade))
    elif idade == 18:
        print(' Está no momento de se alistar.')
    else:
        print(' Passou {} ano(s) do tempo de seu alistamento militar.'.format(idade-18))
else:
    print(' Como mulher, você não tem obrigação de se alistar.')



