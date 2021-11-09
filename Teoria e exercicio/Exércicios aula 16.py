"""
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20:  '))
    if 0 <= num <= 20:
        break
    resp = '  '
    while resp not in 'SN':
        resp = str(input('Você quer continuar ? [S/N] ')).upper().strip()[0]
        if resp == 'Nn':
            break
        
    print('Tente novamente', end=' ')
print(f'você digitou o número {cont[num]}')
================================================================================
Desafio 73
================================================================================
time = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'Chapecoense')


print(f'Os 5 primeiros são {time[0:5]}')
print('-='*15)
print(f'Os últimos 4 colocados são {time[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(time)}')
print('-='*15)
print(f'A chapecoense está na posição {time.index("Chapecoense")+1}ª posição')

================================================================================
Desafio 74
from random import randint
menor = maior = 0
numeros = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10) )

print('os valores sorteados foram:', end= ' ')
for n in numeros:
    print(f'{n} ', end=' ')
    
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
================================================================================
Desafio 75
================================================================================
n = (int(input(f'Digite um numero : ')),
 int(input(f'Digite outro numero: ')),
 int(input(f'Digite mais um número: ')),
 int(input(f'Digite o último numero : ')))

print(f'Você digitou os valores {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes')

if 3 in n:
    print('Os valores pares digitados foram  ', end= ' ')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end= ' ')
for n in n:
    if n % 2 ==0:
        print(n, end=' ')
        
================================================================================
Desafio 76
n = (int(input(f'Digite um numero : ')),
 int(input(f'Digite outro numero: ')),
 int(input(f'Digite mais um número: ')),
 int(input(f'Digite o último numero : ')))

print(f'Você digitou os valores {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes')

if 3 in n:
    print('Os valores pares digitados foram  ', end= ' ')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end= ' ')
for n in n:
    if n % 2 ==0:
        print(n, end=' ')
================================================================================
lista = ('Cadeira',  100.00, 
        'Mesa', 600.00 )

print('-'*30)
print('Listagem de Preço')
for pos in range (0,len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}')
    else:
        print(f'{lista[pos]}')

 materiais = ('Lapis', 200,
            'caneta', 100 )
================================================================================

for pos in range(0,len(materiais)):
    if pos % 2 ==0:
        print(f'\n{materiais[pos]:.<30}',end=' ')
    else:
        print(f'R$ {materiais[pos]} ' )    

================================================================================
Desafio 77
================================================================================
words = ('lapis', 'caneta', 'curso','aprendizado','proparoxitona')

for w in words:
    print(f'\nNa palavra {w} temos as vogais:  ', end=' ')
    for letra in w:
        if letra.lower() in'aeiou':
            print(letra, end=' ')
================================================================================
"""


    
