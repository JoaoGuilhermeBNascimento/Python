"""
Desafio 90
========================================
nome = dict()
media = dict()
ficha = list()

nome = str(input('Nome: '))
media = float(input('Media: '))
ficha.append(nome)
ficha.append(media)
print(f'Nome é igual a {ficha[0]}')
print(f'Média é igual a {ficha[1]}')
if media >= 6:
    print(f'A situação de {ficha[0]} é APROVADO')
else:
    print(f'A situação de {ficha[0]} é REPROVADO')
========================================
2ª Forma
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >=7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print(aluno)
print('-='*30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')

========================================
Desafio 91
========================================
maior = 0
from operator import itemgetter
from random import randint
from time import sleep
jogo = { 'Jogador1': randint(1,6),
'Jogador2': randint(1,6),
'Jogador3': randint(1,6),
'Jogador4': randint(1,6)
}
ranking = list()
print('=-'*30)
for k, v in jogo.items():
    print(f'{k} tirou  {v} no dado')
    
ranking = sorted(jogo.items(),key=itemgetter(1), reverse=True) # itemgetter, para ordenar os itens do dicionário
print(ranking)
print('=-'*30)

print('=-'*30)
print('  ==RANKING DOS PLAYERS==')
for i, v in enumerate(ranking): # não utilizou items porque o ranking está sendo tratado como uma lista
    print(f'  {i+1}º lugar: {v[0]} com {v[1]}')
    print('=-'*30)
    sleep(0.5)
========================================
Desafio 92
========================================
from datetime import datetime
ficha = dict()

ficha['nome'] = str(input('Nome:'))
nasc = int(input('Ano de nascimento: '))
ficha['idade'] = datetime.now().year - nasc
ficha['Carteira'] = int(input('Carteira de trabalho: '))
if ficha['Carteira'] != 0:
    ficha['ano de contratação'] = int(input('Ano de contratação: '))
    ficha['salario'] = float(input('Qual o salário: R$ '))
    ficha['aposentadoria'] = ficha['idade'] +(ficha['ano de contratação'] + 35) - datetime.now().year
print('=-'*30)
for k, v in ficha.items():
    print(f'   - {k}:  {v}')
========================================
Desafio 93
========================================    
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
========================================
Desafio 94
========================================    
dados = dict()
ficha = list()
soma = media = 0

while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))

    while True:
        dados['sexo']= str(input('sexo: [M/F] ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('Error! Digite apenas M ou F!')
    dados['idade']= int(input('Idade: '))
    soma += dados['idade']
    ficha.append(dados.copy())

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper() .strip()[0]
        if resp in 'SN':
            break
        print('Error! Responda apenas S ou N...')
    if resp == 'N':
        break
print('=-'*30)
print(ficha)
print(f'O total de pessoas cadastradas foram {len(ficha)}...')
media = soma / len(ficha)
print(f'A média de idade do grupo é {media} anos')
print('As mulheres cadastradas foram', end=' ')
for p in ficha:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print( )
print('D) Lista das pessoas que estão acima da média: ', end=' ')
for p in ficha:
    if p['idade'] >= media:
        print('  ')
        for k, v in p.items():
            print(f' {k} = {v};',end=' ')
        print()
========================================
Desafio 95
========================================            
    
"""
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome: '))    
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou ? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:   
        resp = str(input('Quer continuar ? [S/N] ')).upper() .strip()[0]
        if resp in 'SN':
            break
        print('Error! digite apenas S ou N...')
    if resp in 'N':
        break
print('-='*30)
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end=' ')
print()
print('-'*30)
for k, v in enumerate(time):
    print(f'{k+1:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}, ',end=' ')
    print()
print('=-'*30)
while True:
    busca = int(input('Mostrar dados de qual jogador ? (999 interrompe) '))
    if busca == 999:
        break
    if busca >= len(time+1):
        print(f'Error! Não existe jogador com o código da {busca}')
    else:
        print(f' ---Levantamente do Jogador {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1 } fez {g} gols')
    print('-'*40)
print('<<Volte sempre>>')
