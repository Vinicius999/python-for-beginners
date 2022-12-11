import random
a1 = input(' 1º aluno: ')
a2 = input(' 2º aluno: ')
a3 = input(' 3º aluno: ')
a4 = input(' 4º aluno: ')
list = [a1, a2, a3, a4]
random.shuffle(list)
print(' A sequência será {}\n'.format(list))
