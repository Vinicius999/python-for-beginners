pal = 'mesa', 'carro', 'python', 'javascript', 'marmelada',\
      'dinheiro', 'mamuxquinha', 'filme', 'terror', 'anarcocapitalismo'
for cp in pal:
    print(f'Na palavra ¨{cp.upper()}¨ temos ', end=' ')
    for cl in cp:
        if cl in 'aáâêéíóôúeiou':
            print(cl, end=' ')
    print('')

