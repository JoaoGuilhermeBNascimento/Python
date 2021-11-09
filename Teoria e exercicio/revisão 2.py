"""
aluno = dict()


while True:
    aluno ['nome'] = str(input('Nome: '))
    aluno ['media'] = float(input(f'Média de {aluno["nome"]}: '))

    if aluno['media'] >= 7:
        aluno['Situação'] = 'Aprovado'
    elif 5 <= aluno['media'] < 7:
        aluno['Situação'] = 'Recuperação'
    else:
        aluno['Situação'] = 'Reprovado'
    print(aluno)    
    print('-='*30)
    for k, v in aluno.items():
        print(f'{k} é {v}')
    resp = str(input('Quer continuar ? [S/N] ')).upper().strip()[0]
    if resp in 'N':
        print('Volte sempre')
        break

from random import randint
from operator import itemgetter
jogo = {'jogador 1':randint(1,6),
'jogador 2':randint(1,6),
'jogador 3':randint(1,6),
'jogador 4':randint(1,6)
}
ranking = list()
print('=-'*30)
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
ranking = sorted(jogo.items(),key=itemgetter(1),reverse=True)
print(ranking)
print('=-'*30)
print('  ===RANKING===   ')
for i, v in enumerate(ranking):
    print(f' {i+1}º lugar: {v[0]} com {v[1]}')

ficha = dict()
from datetime import datetime
ficha['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento ?  '))
ficha['idade'] = datetime.now().year - nasc
ficha['carteira de trabalho: '] = int(input('Carteira de trabalho:  (0 não tem) '))
if ficha['carteira de trabalho: '] != 0:
    ficha['Ano de contratação'] = int(input('Ano de contratação: '))
    ficha['Salário'] = float(input('Salário : R$ '))
    ficha['Aposentadoria'] = ficha['idade'] + ((ficha['Ano de contratação'] + 35) - datetime.now().year)
elif ficha['carteira de trabalho: '] == 0:
    print('Você não tem registro de CTPS')
print('=-'*30)
for k, v in ficha.items():
    print(f'- {k} : {v}')

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou ?'))

for c in range(0,tot):
    partidas.append(int(input(f'Quantos gols na  {c}º partida ?')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('=-'*30)

for k, v in jogador.items():
    print(f'{k} : {v}')
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(partidas):
    print(f' => Na partida {i}, fez {v} gols.')


dados = dict()
ficha = list()
soma = media = 0
cont = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome : '))

    while True:

        dados['sexo'] = str(input('Sexo [M/F] → ')).upper().strip()[0]
        if dados['sexo'] in 'MF':
            break
        print('Error! Digite apenas M ou F')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    
    ficha.append(dados.copy())

    while True:
        resp = str(input('Quer continuar ? [S/N]')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N...')
    if resp == 'N':
        break
        
media = soma / len(ficha)
print(ficha)

print(f'O total de pessoas cadastradas é {len(ficha)}')
print(f'A média das idades de é {media:5.2f}')
print('As mulheres cadastradas foram', end=' ')
for p in ficha:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end= ' ')
print()

time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear
    jogador['nome'] = str(input('Nome: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou ? '))
    partidas.clear()
    for c in range (1,tot+1):
        partidas.append(int(input(f'Quantos gols na {c}º partida ? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar ? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Error! Digite apenas S ou N...')
    if resp in 'N':
        break
print('=-'*30) 
print('cod ', end=' ')
for i in jogador.keys():#cabeçalho
    print(f'{i:<15}', end=' ')
print()
print('=-'*30)
for k, v in enumerate(time):
    print(f'{k:> 3} ', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')  
    print()
while True:
    busca = int(input('MOstrar dados de qual jogador ?  (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! não existe jogador com código da {busca}')
    else:
        print(f'--- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols')
    print('='*40)


função

def soma(a,b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


soma(4,5)
soma(8,9)
soma(2,1)
soma(3,9,5)

def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')
    


contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)
def area(base, altura):
    a = (base * altura)/2
    print('--='*20)
    print(f'A área do triangulo é {a}')


alt = float(input('Altura (M): '))
bas = float(input('Base (M): '))
area(alt, bas)
"""
def maior(* num):
    cont = maior = 0
    print('\nAnalisando os valores informados...')
    for valor in num:
        print(f'{valor}',end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont +=1
    print(f'Foram informados{cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')



maior(2,6,4,1,2,8)
maior(8,0)
maior(4,8,32,4)
