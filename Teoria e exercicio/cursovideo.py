"""
n1 = int(input('Digite um valor:')) 
n2 = int(input("digite outro: "))

s = n1 + n2
#print('A soma entre', n1 ,'e', n2,"vale:",s), metodo antigo.

print("a soma entre {} e {} vale {}".format(n1, n2, s))


a = input('digite algo: ')
print("O tipo primitivo desse valor é", type(a))
print("só tem espaços ?", a.isspace())
print("só tem letras maiusculas", a.isupper())
print("só tem decimal", a.isdecimal())
print("só tem alfabético", a.isalpha())
print("só tem alfanúmerico", a.isalnum())
 
 ** = potência
 // = Divisão inteira
 %  = resto da divisão
 
 Ordem de precedência 
 1 - () 2 - ** 3 - * / // % 4 - + e =
 nome = input('Qual é o seu nome: ')
print('Prazer em te conhecer {:=^10}'.format(nome))

end=' ' = no final do print para não pular a linha para o de baixo utilizar esse comando
alt + 92 para fazer contra barra \
    \n  para quebrar a linha 
    ###################
    n1 = int(input('Um valor: '))
n2 = int(input('outro valor:  '))
s = n1 + n2
m = n1* n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n o produto é {} e a divisão é {:.3f},\n a divisão inteira é {} e a exponenciação é {} '.format(s, m, d, di, e))
 --------------------------------------------------------------------------------- 
# desafio 05
n = int(input('Digite um número inteiro: '))

s = n + 1
a = n - 1

print('O seu sucessor é {} e o seu antecessor é {}'.format(s, a))
--------------------------------------------------------------------------------
n = int(input('Informe um número: '))

d = n * 2
t = n * 3
r = n **(1/2)

print('O número é {} seu dobro é {} seu triplo é {} e sua raiz quadrada é {}'.format(n, d, t, r))

n1 = int(input("Nota do primeiro bimestre: "))
n2 = int(input('Nota do segundo bimestre: '))

m = (n1 + n2) /2
print('A média é : {}'.format(m))

if m >= 6:
    print('Parábens, você está aprovado')
else:
    print('Você está de recuperação')
    1 = 100 cm
    1cm = 10 mm
-------------------------------------------------------------------------------
Desafio 8
n = float(input('Cite um valor em metros: '))

c = n * 100

m = c * 10

print('O valor de {} metros, convertido para Centimetros é {} e para milímetros é {}'.format(n, c, m))
------------------------------------------------------------------------------
n = int(input('Informe um número inteiro: '))

t = n * 1, n * 2, n * 3, n * 4, n * 5, n * 6, n * 7, n * 8, n * 9 and n * 10

print("A tabuada do número {} é {}".format(n, t))
 2 modo de fazer + bonito
 n = int(input('Digite um número para ver sua tabuada:  '))

print('{} x {} = {}'.format(n, 1, n*1))
print('{} x {} = {}'.format(n, 2, n*2))
print('{} x {} = {}'.format(n, 3, n*3))
print('{} x {} = {}'.format(n, 4, n*4))
print('{} x {} = {}'.format(n, 5, n*5))
print('{} x {} = {}'.format(n, 6, n*6))
print('{} x {} = {}'.format(n, 7, n*7))
print('{} x {} = {}'.format(n, 8, n*8))
print('{} x {} = {}'.format(n, 9, n*9))
print('{} x {} = {}'.format(n, 10, n*10))
------------------------------------------------------------------------------
r = float(input('Quanto de dinheiro você possui: '))

compra = r / 3.27

print("Com R$ {} você Pode comprar {:.2f} dolares".format(r ,compra))

l = float(input('Informe a largura da parede: '))
a = float(input('Informe a altura da parede: '))
------------------------------------------------------------------------------
area = l * a
print(area)
tinta = area / 2
print('Sua parede tem dimensão de {} x {} e sua área é de {} \n para pintar essa parede, será necessário {}L de tinta.'.format(l, a, area, tinta))
------------------------------------------------------------------------------
preço = float(input('Qual o preço do produto ? : '))

preço_com_desconto = preço * 0.05

preço_final = preço - preço_com_desconto

print(' O preço do produto é {} com 5% de desconto fica {:.2f}'.format(preço, preço_final))
------------------------------------------------------------------------------
salárioinicial = float(input('Qual salário do Funcionário ? R$ '))
 
aumento = salárioinicial *0.15

salário_final = salárioinicial + aumento

print("O seu salário era de {}, com 15% de aumento foi para {}".format(salárioinicial, salário_final))
------------------------------------------------------------------------------
c = float(input(' Informe a temperatura em ºC: '))
f = ((9 * c)/ 5) +32

print('A temperatura de {} º C convertida para ºF é {}'.format(c, f))
------------------------------------------------------------------------------
d = float(input('Você deseja alugar o carro por quantos dias ? '))

k = float(input('Quantos km foram rodados neste veiculo após alugado ? '))


total = (d * 60) + (k * 0.15)

print('O total a pagar é de R$ {:.2f}'.format(total))
------------------------------------------------------------------------------
Aula 08 - 

Quando importamos a biblioteca math, temos varias funcionalidades entre elas:
 - ceil - que faz arredondamentos para cima
 - floor - que faz arredondamentos para baixa
 - trunc - vai eliminar da virgula pra frente, vai truncar
 - pow - é potencia
 - sqrt - raiz quadrada 
 - factorial - numero fatorial 
     para utilizar somente uma funcionalidades, vamos fazer o uso do from math import sqrt
     Ctrl+ espaço aparece funcionalidade do import
------------------------------------------------------------------------------

from math import sqrt,ceil,floor,pow
num = int(input('Digite um número: '))

raiz = sqrt(num)

print("a raiz de {:.2f} é igual a {:.2f}".format(num,ceil(raiz)))

Numeros random
import random 
num = random.randint(1, 5)
print(num)

import emoji
print(emoji.emojize("olá mundo: ::new_moon_with_face::", use_aliases=True))

print(emoji.emojize("olá mundo! :earth_americas:", use_aliases=True))
------------------------------------------------------------------------------
Desafio 16
from math import trunc
n = float(input('Digite um número inteiro:'))
print('O número digitado é {} tem a parte inteira {}'.format(n, trunc(n)))
#outro metodo
n = float(input("Digite um numero: "))
print("O número digitado é {} e a sua porção inteira é {}".format(n, int(n)))
------------------------------------------------------------------------------
Desafio 17
cadj = float(input('Informe o cateto adjacente do triângulo: '))

copos = float(input('Informe o cateto oposto do triangulo: '))

hipo = (cadj**2 + copos**2) ** (1/2)
print('O cateto adjacente é {} o cateto oposto é {} e o comprimento da hipotenusa é {:.2f}'.format(cadj, copos, hipo))
------------------------------------------------------------------------------ 2 forma 
import math

ca = float(input("Comprimento do cateto adjacente:"))
co = float(input('Comprimento do cateto oposto: '))

hi = math.hypot(ca, co)

print('Comprimento da hipotenusa é {:.2f}'.format(hi))
------------------------------------------------------------------------------ 
Desafio 18
Ex: 1
import math

a = float(input('Informe um ângulo:'))

seno = math.sin(math.radians(a))
coseno = math.cos(math.radians(a))
tangente = math.tan(math.radians(a))

print('O ângulo de {} tem o valor para seno de {:.2f}, de coseno  {:.2f} e da tangente {:.2f}'.format(a,seno, coseno, tangente))

ex 2 : 
 from math import radians, sin, cos, tan
a = float(input('Informe um ângulo:'))

seno = sin(radians(a))
coseno = cos(radians(a))
tangente = tan(radians(a))

print('O ângulo de {} tem o valor para seno de {:.2f}, de coseno  {:.2f} e da tangente {:.2f}'.format(a,seno, coseno, tangente))

#### UMA LISTA FICA ENTRE COLCHETES 
------------------------------------------------------------------------------ 
DESAFIO 19
from random import choice, sample, shuffle
#import random
a = str(input('Digite o nome de um aluno: '))
b = str(input('Digite o nome de um aluno: '))
c = str(input('Digite o nome de um aluno: '))
d = str(input('Digite o nome de um aluno: '))
list = [a, b, c, d]
escolhido = choice(list)

print('O aluno escolhido foi {}'.format(escolhido))
------------------------------------------------------------------------------ 
desafio 20
from random import choice, sample, shuffle
#import random
a = str(input('Digite o nome de um aluno: '))
b = str(input('Digite o nome de um aluno: '))
c = str(input('Digite o nome de um aluno: '))
d = str(input('Digite o nome de um aluno: '))
list = [a, b, c, d]
shuffle(list)

print('A ordem escolhida é {}'.format(list))
------------------------------------------------------------------------------ ------------------------------------------------------------------------------ 
desafio 021
import pygame

pygame.init()

pygame.mixer.music.load('wolf.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input('agora voce escuta')
------------------------------------------------------------------------------ ------------------------------------------------------------------------------ 
Aula 09
- Fatiamento

fase[9:21:2]
sempre colocar um número a mais no final do fatiamento de range, o último valor não entra na contagem 
frase[:5] - Quando eu nao coloco onde ele vai começar, ele começa do caractere 0 sendo a mesma coisa que colocar [0:5],
o mesmo acontece se fizermos ao contrário, no caso [15:0] do 15 caractere ao fim

     No caso de [9::3] ele vai até o fim, pulando de 3 em 3 caracteres 

- Análise de string
    len(frase) = len - significa comprimento
    frase.count('o') - pedindo ao programa pra contar, quantas vezes aparece a letra o minuscula, caso tenha O maiusculo, ele não contará
    frase.count('o', 0, 13) - nesse caso ele vai contar a letra O e imprimir quantas letras O tem do caractere 0 até o 13.
    frase.find('deo',) - 
    frase.find('Android') - se voce coloca uma string dentro do find e não tem na frase, o resultado é -1
    'curso' in frase 
- Transformação 
    frase.replace('Python', 'Android') - nesse caso, o python será substituido por 'Android'
    frase.upper() - o que for maiusculo ele mantém, o que estiver em minusculo ele coloca em maiusculo 
    frase.lower() - o contrário do upper.
    frase.capitalize() - ele joga os caracteres para minusculo e a primeira letra da frase ele coloca em maiusculu
    frase.title() - ele torna o caractere inicial de cada palavra em maiusculo 
    frase.strip() - ele remove todos os espaços inuteis no inicio e no final da string
    frase.rstrip() - onde o R e right- começa a tratar pela direta, removendo apenas os últimos espaços 
    frase.lstrip() - onde o L e left- começa a tratar pela esquerda, removendo apenas os últimos espaços 
- Divisão 
    frase.split()  - vai ocorrer uma divisão dentro da string, cada palavra recebe uma indexação nova, separando cada palavra em uma lista, tornando cada palavra um número
- Junção
    '-'.join(frase) - voce vai juntar todos os elementos da frase e usar o - como separador por ex. Curso-em-video-python
    frase = 'Curso em Vídeo Python'
    frase = frase.replaced('Python', 'Android) - > double atribuition
    print(frase.lower().find('Vídeo'))
------------------------------------------------------------------------------ ------------------------------------------------------------------------------ 

dividido = frase.split()
print(dividido[3])
frase = 'Curso em Vídeo Python'

dividido = frase.split()
print(dividido[2] [3])
# resultando na letra 'e'
frase = ("Curso em Video Python")

dividido = (frase.split())
print(dividido[3] [5]) # resulta em 'n' a quarta palavra e a sexta letra 
------------------------------------------------------------------------------ ------------------------------------------------------------------------------ 
Desafio 022
nome = str(input('Informe o seu nome: ')).strip()

print('seu nome em maiúsculas é {}'.format(nome.upper()))
print('seu nome em minúsculas é {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' '))) --> nessa função ele vai contar quantos espaços tem com espaço = o contador de espaços com o strip aplicado no inicio
#print('seu primeiro nome tem {} letras'.format(nome.find(' '))) --> nessa ocasião, o find buscou o primeiro espaço de um nome para o outro, definindo onde estaria o 1 nome
separa = nome.split()
print(separa)
print('seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))------- ------------------------------------------------------------------------------ 
Desafio 023
"""
"""
num = int(input('Informe um número : '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}:'.format(d))
print('Centena: {}'.format(c))
print('Milhar:{}'.format(m))
------------------------------------------------------------------------------ ------------------------------------------------------------------------------ 
Desafio 024
cid = str(input('Em qual cidade você nasceu ? ' )).strip()
print(cid[:5].upper() == 'SANTO')
------------------------------------------------------------------------------ ------------------------------------------------------------------------------ 
Desafio 025
nome = str(input('Qual o seu nome ?')).strip()

print('seu nome nome tem Silva ? {} '.format('SILVA' in nome.upper()))  
------------------------------------------------------------------------------ ------------------------------------------------------------------------------ 
Desafio 026 
n = str(input('Informe uma frase:  ')).lower().strip()

print('A letra "a" aparece {} vezes'.format(n.lower().count('a')))
print('A posição que ele aparece a primeira vez é {}'.format(n.find('a')+1))
print('A posição que ele aparece por último é {}'.format(n.rfind('a')-1))
------------------------------------------------------------------------------ ------------------------------------------------------------------------------ 
Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
n = str(input('Informe seu nome completo: ')) .strip()
nome = n.split()

print('primeiro = {}'.format(nome[0]))
print('último = {}'.format(nome[len(nome)-1]))
------------------------------------------------------------------------------ ------------------------------------------------------------------------------ 


"""

n = str(input('Informe seu nome completo: ')) .strip()
nome = n.split()

print('primeiro = {}'.format(nome[0]))
print('último = {}'.format(nome[len(nome)-1]))