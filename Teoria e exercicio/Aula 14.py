"""
while - enquanto não chegar ao objetivo ele fica agindo, usar while quando não saber o limite

while not x:
    if:
        passo
    if:
        pula
    if:
        pega
pega (está fora porque chegou ao final, alcançou o objetivo)

for c in range(1,10):
    print(c)
print('fim')
# para while a gente começa com c = 1, que é o começo do range (1,10)
c = 1
while c < 10:
    print(c)
    c = c+ 1 # ou C +=1
print('Fim')
n = 1 
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')
##################### desta aforma a baixo identificamos se quer que o programa continue rodando
#sem determinar um range
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar ? [S/N]')).upper()
print('Fim')
## para saber se é par ou impar é contar a quantia deles 
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n !=0:
        if n % 2 == 0:
            par += 1
        else:
            impar +=1
print('Você digitou {} numeros pares e {} números impares!'.format(par, impar))
Exercício 57
sexo = str(input('INforme seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo')).strip().upper()[0]
print('sexo {} registrado com sucesso'.format(sexo))

------------------------------------------------------------------------------------------------
Exercício 58
tentativas = 0
from random import randint
computador = randint(0,10)
print('Sou seu computador...Acabei de pensar no número entre 0 e 10')
acertou = False
while not acertou:
    jogador = int(input('Qual é o seu palpite:  '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez')
        elif jogador > computador:
                print('Menos...Tente mais uma vez')
print('Acertou')
print('VocÊ teve {} tentativas até acertar'.format(tentativas))
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
exercício 59
from time import sleep
n1 = int(input('Informe um valor:'))
n2 = int(input('Informe mais um valor: '))
opção = 0
soma = n1+n2
multiplicar = n1*n2
while  opção != 5:
    print("O que você deseja :
[1] SOMAR
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa  
")
    opção = int(input('Qual é a sua opção: '))
    if opção == 1:
        print('A soma entre {} + {} e {}'.format(n1, n2,soma))
    elif opção ==2:
        print('A multiplicação de {} x {} e {}'.format(n1, n2, multiplicar))
    elif opção ==3:
        if n1 > n2:
            print('O maior é {}'.format(n1))
        else:
            print('O maior é {}'.format(n2))
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Informe um valor:'))
        n2 = int(input('Informe mais um valor: '))
    else:
        print('Opção inválida. tente novamente')
    print('=--='*20)
    sleep(2)
print('Fim do programa, Volte sempre!')
exercício 60

from math import factorial
num = 1
while num >= 1:
    num = int(input('Informe um número: ')) 
    fat = factorial(num)
    print(' O fatorial do número {} é {}'.format(num, fat))

if num <= 0:
    print('Número invalido')
######### 2 FORMA 
   n = int(input('Digite um número para calcular seu fatorial: '))
c = n 
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end= '')
    print(' x' if c > 1 else '=', end='')
    f *= c
    c -= 1
print('{}'.format(f))
-=----------------------------------------------------
print('Gerador de PA')
print('-='*10)
primeiro_termo = int(input('Informe o primeiro termo desejado:  '))
razao = int(input('Qual a razão desejada:  '))
termo = primeiro_termo
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} → '.format(termo), end= '')
        termo += razao
        cont +=1
    print('PAUSA')
    mais = int(input('Quabntos termos você quer mostrar a mais? '))
print('Progressão finaliada com {} termos mostrados'.format(total))

exercício 
#  os números seguintes serão a soma dos dois números anteriores, ficando desta forma: 0, 1, 1, 2, 3, 5, 8, 13, 21
print('-' * 30)
print('Sequência de Fibonacci')
print('--'*30)
n = int(input('quantos termos você quer mostrar : '))
t1 = 0
t2 = 1
print('--'*30)
print('{} → {}'.format(t1, t2), end='')
cont = 3 # começou no 3 termo porque  ja mostrou o primeiro termo e o segundo termos
while cont <= n:
    t3 = t1 + t2
    print(' → {}  '.format(t3), end='')
    t1 = t2 
    t2 = t3
    cont += 1
print(' → FIM')
print('--'*30)


"""
primeiro = int(input('Informe o primeiro termo da PA:  '))
razao = int(input('Informe a razão desejada: '))
opçao = 0
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} → '.format(termo), end=' ')
        termo += razao
        cont +=1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais ?'))

print('Progressão finalizada com {} termos mostrados'.format(total))
