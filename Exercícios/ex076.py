list = 'Paçoquinha', 8.20, 'Livro', 224.90,\
       'Barata Doce', 3.00,'Frango', 8.50, 'Ovos', 11.50,\
       'Arroz', 3.20, 'Macarrão', 2.50, 'Cuscuz', 0.99
print('-'*45)
print(f'{"LISTAGEM DE PREÇOS":^45}')
print('-'*45)
for c in range(0, len(list), 2):
    print(f'{list[c]:.<35}R${list[c+1]:>7.2f}')
print('-'*45)