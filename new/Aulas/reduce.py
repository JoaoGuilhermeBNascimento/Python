from dados import*
from functools import reduce

# reduce é uma função acumuladora

""" 
======================
# sem reduce
acumula = 0
for item in lista:
    acumula += item

print(acumula)
============ 
#soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
# a cada volta do laço, ela vai executar i + ac ( 1+0) e guardar o valor na variável ac e e executar somando (1+2) e assim vai.
#print(soma_lista)

soma_preços = reduce(lambda ac, p: p['preço'] + ac, produtos,0)
print(soma_preços / len(produtos))
"""
#                           :acumulador ,idade do dic, dic que contém idade, é com qual valor vou começar
soma_idade = reduce(lambda ac, p: ac + p['idade'], pessoas,0)
print(soma_idade / len(pessoas))