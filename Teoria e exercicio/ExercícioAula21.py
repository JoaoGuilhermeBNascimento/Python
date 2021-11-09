
"""
========================
EXERCÍCIO 101
========================
from datetime import datetime
def voto(ano):
    
    idade = datetime.now().year - ano
    if idade < 16:
        return f'com {idade} anos: NÃO VOTA. '
    elif 16 <= idade < 18 or idade > 65:
        return f'com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    return idade


ano = int(input(f'Ano de nascimento: '))
print(voto(ano))
========================
EXERCÍCIO 102
========================
def fatorial(n=1, show=False):
    ""[summary]

    Args: Make the calculation of a fatorial number.
        n (int, optional): [description]. Defaults to 1.
        show (bool, optional): [description]. Defaults to False.

    Returns:
        [type]: [description]
    ""
    f = 1
    for c in range(n,0,-1):
        if show:
            print(c,end=' ')
            if c > 1:
                print(f'x', end=' ')
            else:
                print('=',end=' ')
        f *= c        #f = f * c
    return f

n = int(input('Informe um número: '))
print(fatorial(n,show=True))

========================
EXERCÍCIO 103
========================
def ficha(jog='Desconhecido',gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato')
    


n  = str(input('Nome: '))
g = str(input(f'numero de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == ' ':
    ficha(gol=g)
else:
    ficha(n, g)
========================
print('-'*40)
def fun(nome,gols):
    if nome in'':
        nome='<Desconhecido>'

    if gols in'':
        gols=0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

j=input('Nome do Jogador: ').capitalize()
g=input('Número de gols: ')
fun(j,g)
========================
EXERCÍCIO 104
========================
def leiaint(msg):
    ok = False
    valor = 0 
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Error! Digite um número inteiro válido')
        if ok:
            break
    return valor
========================
EXERCÍCIO 105
========================
def notas(*n, sit=False):
    ""

    --> Função para analisar notas e situações de vários alunos
    Args:
        sit (bool, optional): [description]. Defaults to False.

    Returns:
        [type]: [description]
    ""
    r = dict( )
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] > 7:
            r['Situação'] = 'BOA'
        elif r['media'] >= 5:
            r['Situação'] = 'Razoável'
        else:
            r['Situação'] = 'RUIM'
    return r





resp = notas( 5.5, 6.5, 6.5, sit=True)
print(resp)
help(notas)
========================
EXERCÍCIO 106
========================
c = ('\033[m', #0 - cores)
    '\033[0;30;41m',# 1 - vermelho
    '\033[0;30;42m', # 2 -  verde
    '\033[0;30;43m', # 3 - amarelo
    '\033[0;30;44m', # 4 - azul
    '\033[0;30;45m', # 5 - roxo
    '\033[7;30m' # 6 - branco
);



def ajuda(com):
    help(com)


def titulo(msg):
    tam = len(msg)
    print('~~'*tam)
    print(f'  {msg}')
    print('~~'*tam)


comando = ' '
while True:
    titulo('Sistema de ajuda Pyhelp')
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo')
"""
