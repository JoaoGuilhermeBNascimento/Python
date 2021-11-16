""" from dados import *
# MAPEAMENTO DE LISTA
# nova_lista = map(lambda x: x * 2, lista)
nova_lista = [x * 2 for x in lista]
print(lista)
print(list(nova_lista))
from dados import *

preço = map(lambda p: p['preço'], produtos)

for preço in preço:
    print(preço*0.2)
 

# MAPEAMENTO DE DICTIONARY

from dados import *


def aumenta_preço(p):
    p['preço'] = round(p['preço'] * 1.05, 2)
    return p



novos_produtos = map(aumenta_preço, produtos)

for produto in novos_produtos:
    print(produtos)
 
from dados import*
nomes = map(lambda p: p['nome'], pessoas)
idade = map(lambda i:i['idade'], pessoas)
for pessoas in nomes:
    print(pessoas)
print()
for pessoas in idade:
    print(pessoas)
    """
# dessa forma eu isolo o conteúdo do dicionário, como no caso do dict(pessoas) eu isolo a idade e o nome

from dados import*

def aumenta_idade(p):
    p['nova_idade'] = round(p['idade']*1.20)
    return p


nomes = map(aumenta_idade, pessoas)

# nomes = map(lambda p: round(p['idade']*1.20), pessoas)


for pessoas in nomes:
    print(pessoas)

