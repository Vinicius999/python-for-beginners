sexo = input(' Informe seu sexo: [M/F] ').upper().strip()[0]
while sexo not in 'MmFf':
    sexo = input(' \033[31mDados inválidos!\033[m\n Informe seu sexo: [M/F] ').upper().strip()[0]
print(' Sexo {} registrado com sucesso!'.format(sexo))