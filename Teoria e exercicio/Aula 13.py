"""
for C in range(0,3)

for c in range (6,0, -1): ###SE QUISER CONTAR PARA TRAS TEM QUE COLOCAR , -1
    print(c)
print('FIM')

n = int(input('Digite um número:' ))
for c in range(0,n+1):
    print(c)
print('FIM')

i = int(input('Início: '))
f = int(input('FIM:'))
p = int(input('Passo:'))

for c in range (i, f+1, p):
    print(c)
print('Fim')

#### Nesta situação  eu posso colocar para entrar quantos números eu quiser  variando o (0, X)
s = 0
for c in range(0,3):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))
exercício 46
from time import sleep
print('Contagem Regressiva para estouro de fogos')
from time import sleep
print('Contagem Regressiva para estouro de fogos')
for c in range(10,-1,-1):
    sleep(1)
    print(c)
print('Fim')
Exercício Python #047 - Contagem de pares
print('Os números entre 1 e 50 pares são:')
for c in range(1,51):
    n = c % 2
    if n == 0:
        print(c)
print('Fim')
####### 2 FORMA DE FAZER 
print('Os números entre 1 e 50 pares são:')
for n in range(1,51):
    if n % 2 ==0:
        print(n, end=' ')
print('Fim')
##### 3 forma de fazer
for n in range(2,51,2):
    print(n,end=' ')
print('Acabou')
Exercício Python #048 - Soma ímpares múltiplos de três
s = 0

for n in range(1,501,2):
    if n % 3 ==0:
        s +=n 
print('O somatório de todos os valores é {}'.format(s))
### 2 FORMA MAIS COMPLETA 
s = 0
cont = 0
for n in range(1,501,2):
    if n % 3 ==0:
        cont = cont + 1
        s +=n 
print('A soma de todos os {} valores solicitados é {}'.format(cont,s))
Exercício Python #049 - Tabuada v.2.0
num = float(input('Qual a tabuada desejada ?'))

for n in range(1, 11):
    print('{:.0f} x {:.0f} = {:.0f}'.format(num, n , num*n))

Exercício 50
soma = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2== 0:
        soma = soma + num # pode ser simplificado como s +=1
        cont = cont + 1 # pode ser simplificado como cont +=1
print('Você informou {} números pares e a soma foi {}'.format(cont, soma))
exercício 51
primeiro_termo = int(input('Qual o primeiro termo ? '))
razao = int(input('Qual a razão da PA desejada ?'))
decimo = primeiro_termo+(10-1) * razao
for c in range(primeiro_termo, decimo+razao, razao):
    print('{}'.format(c), end=' → ')
print('FIM')
Exercício 52
tot = 0
num = int(input('Digite um número inteiro: '))
for c in range(1, num +1):
    if num % c ==0:
        print('\33[33m', end = ' ')
        tot += 1
    else:
        print('\033[31m', end = '')
    print('{} '.format(c), end ='')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot ==2:
    print('esse número é primo')
else:
    print('O número não é primo')
exercício 53 
frase = str(input('Digite uma frase:  ')) .strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
### inverso = ''
inverso = junto[::-1]
'''for letra in range(len(junto)-1, -1, -1):
   inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))  
if inverso == junto:
    print('temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo')
Exercicio 54
from datetime import date
atual = date.today().year
totamaior =0
totamenor =0
for pess in range(1,8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu ? '.format(pess)))
    idade = atual - nasc

    if idade >= 18:
        totamaior +=1
    else:
        totamenor +=1
print('Ao todo  tivemos {}  pessoas maiores de idade '.format(totamaior), end= ' ')
print('E também tivemos {} pessoas menores de idade'.format(totamenor))
exercício 56
maior = 0
menor = 0
for pess in range(1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(pess)))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}kg'.format(maior))
print('O menor peso lido foi de {}kg'.format(menor))
exercício 56
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
totmulher20 = 0
for p in range (1,5):
    print('-----------{}ª PESSOA------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]:')).strip()
    soma_idade += idade
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm'and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 +=1
media_idade = soma_idade /4
print('A média de idade do grupo é de {} anos'.format(media_idade))
print('O homem mais velho tem {} anos é se chama {}'.format(idade, nome_velho))
print('Ao todo são {} mulheres com menos de 20 anos '.format(totmulher20))

"""
