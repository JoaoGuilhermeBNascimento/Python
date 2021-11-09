import moeda


"""
import moeda
n = float (input('Digite o preço: R$ '))
print(f'A metade de {n} é {moeda.metade(n)} ')
print(f'O dobro de {n} é {moeda.dobro(n)} ')
print(f'Aumentando 10% de {n}, temos {moeda.aumento(n)} ')
print(f'Reduzindo 13% de {n}, temos {moeda.diminuir(n)}')
"""
# 2 formas de se fazer
from moeda import metade,dobro,aumento,diminuir,

n = float (input('Digite o preço: R$ '))
print(f'A metade de {n} é {metade(n)} ')
print(f'O dobro de {n} é {dobro(n)} ')
print(f'Aumentando 10% de {n}, temos {aumento(n)} ')
print(f'Reduzindo 13% de {n}, temos {diminuir(n)}')