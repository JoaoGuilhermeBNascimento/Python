"""
Ajuda interativa
- help() - para buscar informações sobre qualquer coisa
- help(print) 
 - Ou ativar no console do python o comando  -- help()
print(input.__doc__)
help(input)
 

 ==============================================
 DOCSSTRINGS
 def contador(i,f,p):
    ""
    --> Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno

    ""
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c +=p
    print('Fim')

help(contador)

===============================
    PARAMETROS OPCIONAIS
def somar(a=0,b=0,c=0):
    ""[summary]

    Args:
        a (int, optional): [description]. Defaults to 0.
        b (int, optional): [description]. Defaults to 0.
        c (int, optional): [description]. Defaults to 0.
    ""
    s = a+b+c
    print(f'A soma vale {s}')

somar(3,2,5)
somar(8,4)
somar() 

==============================================================
        ESCOPO DE VARIÁVEIS 
def teste():
    x = 8 # variavel X com escopo local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}') 


#PROGRAMA PRINCIIPAL
n =2  # variavel N com escolo global

print(f'No programa principal, n vale {n}')
==============================================================
def funcao():
    n1=4
    
    print(f'N1 dentro vale {n1}')


n1 = 2
funcao()
print(f'N1 fora vale {n1}')
==============================================================
def teste(b):
    global a
    a = 8
    b +=4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')

==============================================================
RETORNANDO VALORES
return

def somar (a=0,b=0,c=0):
    s = a + b + c 
    return s



r1 = somar(3,2,5)
r2 = somar(2,2)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}')
============================================================================================================================
Exemplos de exercício utilizando return
==============================================================
def fatorial(num = 1):
    f = 1
    for c in range(num,0,-1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(fatorial(n))
#ou
print(f'O fatorial de {n} é igual a {fatorial(n)} ')
============================================================================================================================
def fatorial(num = 1):
    f = 1
    for c in range(num,0,-1):
        f *= c
    return f # pode retornar valor lógico

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')
============================================================================================================================
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
#print(par(num))
if par(num):
    print('É par!')
else:
    print('Não é Par')
"""
