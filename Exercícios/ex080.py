list = []
for c in range(5):
    n = int(input('Digite um número: '))
    if c == 0 or n > list[-1]:
        list.append(n)
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(list):
            if n <= list[pos]:
                list.insert(pos, n)
                print(f'Adicionado na poisição {pos}...')
                break
            pos += 1
print('-='*20)
print(f'Os valores digitrado em ordem foram {list}')

