""" from dados  import *
# Na filter retorna verdadeiro ou falso, no caso abaixo tudo que estiver abaixo de 5 não aaprece e tudo acima é true aparece
nova_lista = filter(lambda x: x > 5, lista)

print(list(nova_lista))
 
from dados  import *

def filtra(produto):
    if produto['preço'] > 10:
        if produto['preço'] > 50:
            produto['expensive'] = True
        return True
    
    else:
        return False
nova_lista = filter(filtra, produtos)
# nova_lista = filter(lambda p: p['preço'] > 50, produtos)

for produto in nova_lista:
    print(produto)
    # com esse código houve o filtro desses produtos, que o preço é maior que 50
# {'nome': 'p2', 'preço': 55.55}
# {'nome': 'p5', 'preço': 81.23}


from dados import*

def filtra(pessoa):
    if pessoa['idade'] >= 18:
        return True
    if pessoa['idade'] < 18:
        pessoa['Menor de idade'] = True
        return True
    

nova_lista = filter(filtra, pessoas)

for produto in nova_lista:
    print(produto)

"""
