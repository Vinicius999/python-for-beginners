nome = input(' Nome completo: ').strip()
print('-'*35)
print(' Maiúsculo: {}'.format(nome.upper()))
print(' Minúsculo: {}'.format(nome.lower()))
print(' ¨{}¨ contem {} letras.'.format(nome, len(nome) - nome.count(' ')))
# número de caracteres exceto os espaços em branco
first = nome.split()
print(' ¨{}¨ contém {} letras.'.format(first[0], len(first[0])))





