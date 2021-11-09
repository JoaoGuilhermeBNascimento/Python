"""
----------------- Dicionários-------------------
Identificados por {}

dados = dict()
dados = {}


dados = {'Nome':'Pedro','Idade':25}
print(dados['Nome'])
print(dados['Idade'])

dados['sexo'] = 'M' # Para adicionar elementos
del dados['Idade']# para elimitar o elemento idade

filme = {'titulo':'Star Wars',
'ano': 1977,
'diretor':'George Lucas'
}
print(filme.values()) # retorna todos os valores do dicionário
print(filme.keys()) #para pegar a parte de baixo, titulo ano diretor
print(filme.items()) # engloba os 2 

for k,v in filme.items():
    print(f'O {k} é {v}')

-------------------------------------------------------

pessoas = {'nome':'Gustavo','Sexo':'M','Idade':22}
print(pessoas)
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print(f'O {pessoas["nome"]} tem {pessoas["Idade"]} anos')
-------------------------------------------------------
pessoas = {'nome':'Gustavo','Sexo':'M','Idade':22}
del pessoas ['Sexo']       # Apagando o sexo pelo comando del
pessoas ['peso'] = 98.5       # adicionando peso ao dicionário
pessoas ['nome'] = 'Leandro' -      para substituir o nome gustavo por leandro
for k,v in pessoas.items():
    print(f'{k} = {v}')
    # Apagando o sexo pelo comando del
    -------------------------------------------------------
    brasil = []
estado1 = {'Uf':'Rio de Janeiro', 'Sigla':'RJ'}
estado2 = {'Uf':'São Paulo','Sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]) #  = {'Uf': 'Rio de Janeiro', 'Sigla': 'RJ'}
print(brasil[1]) #  = {'Uf': 'São Paulo', 'Sigla': 'SP'}
print(brasil[0]['Uf'])  = Rio de janeiro
print(brasil[1]['Sigla'])  = SP

================================================
.copy() substitui o [:] 

estado = dict()
brasil = list()
for c in range(0,3):
    estado['Uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    print(e) = mostrou cada estado  {'Uf': 'rio', 'sigla': 'rj'}
                                    {'Uf': 'parana', 'sigla': 'pr'}
                                    {'Uf': 'acre', 'sigla': 'ac'}
for e in brasil:
    for k, v in e.items():
        print(f' O campo {k} tem valor {v}') =  O campo Uf tem valor rio
                                                O campo sigla tem valor rj
                                                O campo Uf tem valor sao paulo
                                                O campo sigla tem valor sp
                                                O campo Uf tem valor acre
                                                O campo sigla tem valor ac

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print() # print vazio para pular de linha = Rio de Janeiro RJ 
                                                Sampa SP
                                                Acre AC

aprov['total'] = sum(partidas) - expressão sum para somar 

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou ? '))
for c in range(0, tot):
    partidas.append(int(input(f' Quantos gols na partida {c}')))
jogador['gols'] = partidas[:]
jogador['total']= sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'Ocampo {k} tem o valor {v} ')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i}, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols.')

"""
estado = dict()
brasil = list()
for c in range(0,3):
    estado['Uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)