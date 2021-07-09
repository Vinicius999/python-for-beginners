from utilidadesCeV import moedas
from utilidadesCeV import dados

p = dados.leiaDinheiro('Digite um preço: R$')
moedas.resumo(p, 80, 35)
