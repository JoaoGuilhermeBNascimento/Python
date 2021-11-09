"""
teste = list()
teste.append('Joao')
teste.append(40)
galera = list()
galera.append(teste[:])
teste [0] = 'Maria'
teste [1] = 22
galera.append(teste[:])
print(galera)

Resposta = [['Joao', 40], ['Maria', 22]]

#galera = [['João', 25],['Ana', 33],['Joaquim',50],['Maria', 45]]
#Quatro estruturas compostas dentro de uma 
#print(galera[0][0]) # João
#rint(galera[0]) # ['João', 25]
#for p in galera:
   # print(p) # desta forma eu demonstro todos os nomes e idade
   #print(p[1]) # desta forma mostro apenas as idades
    #print(f'{p[0]} tem {p[1]} anos de idade ')
    # = João tem 25 anos de idade 
    #Ana tem 33 anos de idade 
    #Joaquim tem 50 anos de idade
    #Maria tem 45 anos de idad


totmai = totmen = 0
galera = list()
dados = list ()
for c in range(0,3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
print (galera)
for p in galera:
    if p[1] > 21:
        print(f'{p[0]} é maior de idade')
        totmai +=1
    else:
        print(f'{p[0]} é menor de idade')
        totmen +=1
print(f'temos {totmai} maiores e {totmen} menores')
""" 
"""
=============================================================
Desafio 84
=============================================================

galera = list()
dados = list()
mai = men = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(galera) ==0:
        mai = men = dados[1]
    else:
        if dados [1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    galera.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar ? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(galera)
# print(f'Foram cadastradas {len(galera)} pessoas')
print('=-'*30)
print(f'As pessoas mais pesadas foram {mai} kg. Peso de ', end=' ')
for p in galera:
    if p[1] == mai:
        print(f'[{p[0]}]',end=' ')
print()
print(f'As pessoas  mais leves foram {men} kg. Peso de ',end=' ')
for p in galera:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')
=============================================================
Desafio 85
=============================================================
total = []
par = []
impar = []

for n in range(1,8):
    num = int(input(f'Digite o {n}º valor: '))
    if num % 2 ==0:
        par.append(num)
        
    else:
        impar.append(num)
        
print('Lista com valores Pares',end=' ')
print(sorted(par))
print('Lista com os valores Impares', end=' ')
print(sorted(impar))
=============================================================
2 ª forma
=============================================================
num = [[], []]
valor = 0 
for c in range(1,8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 ==0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('=-'*30)
print(f'Os valores pares digitados foram : {num[0]}')
print(f'Os valores impares digitados foram : {num[1]}')

=============================================================
Desafio 86
=============================================================
matriz = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3):
    for c in range(0,3):
        matriz [l][c] = int(input(f'Digite um valor para [{l},{c}]:'))
print('=-'*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^10}]', end='')
    print()
=============================================================
Desafio 87
=============================================================
matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = mai = scol = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]'))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^10}]', end='')
        if matriz[l][c] % 2 ==0:
            spar += matriz[l][c]
    print()
print('=-'*30)
print(f'A soma dos valores pares é : {spar}')
for l in range(0,3):
    scol += matriz [l][2]
# deixou o L variando e somou com o terceiro valor de todas as listas
# COLUNA ESTÁ FIXA 

print(f'A soma dos valores da terceira coluna é {scol}')
for c in range (0,3): # FIXOU A LINHA E VARIOU A COLUNA
    if c ==0: 
        mai = matriz [1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')
=============================================================
Desafio 88
=============================================================
from random import randint
from time import sleep
lista = []
jogos = []
print('-'*30)
print('           JOGA NA MEGA SENA          ')
quant = int(input('Quantos jogos voce quer que eu sorteie: '))
tot = 1
while tot <=quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot +=1
print('-='*3,f'SORTEANDO {quant} JOGOS', '-='*3)
for i , l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')
    sleep(2)
=============================================================
Desafio 89
=============================================================
ficha = list()
while True:
    nome = str(input('Nome : '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2:  '))
    media = (nota1+nota2)/ 2

    ficha.append([nome, [nota1,nota2], media])
    resp = str(input('Quer continuar ?[S/N] '))
    if resp in 'nN':
        break

print('=-'*30)
print(f'{"No.":<4}{"Nome":<10}{"Media":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('=-'*35)
    opc = int(input('Mostrar notas de qual aluno ? (999 Interrompe):'))
    if opc == 999:
        print('FINALIZANDO')
        break
    if opc <= len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]} ')
print('<<<<<<< VOLTE SEMPRE>>>>>>>')
"""


ficha = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('nota 1 :'))
    nota2 = float(input('nota 2 : '))
    media = (nota1+nota2)/2

    ficha.append([nome,[nota1,nota2],media])
    resp = str(input('Quer continuar ? [S/N] → ')).upper().strip()[0]

    if resp in 'Nn':
        break
print('=-'*30)
print(f'{"No.":<4}{"Nome: ":<10}{"Media":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('Mostrar nota de qual Aluno ?  (999, interrompe)'))
    if opc == 999:
        break
    if opc <= (len(ficha)-1):
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<<<<<<<<volte sempr>>>>>')