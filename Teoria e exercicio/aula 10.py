"""
Aula 10 - 
if carro.esquerda():
    bloco True
else:
    bloco False
    
    tempo = int(input('quantos anos tem seu carro ?'))

if tempo <= 3:
    print('carro novo')

else:
    print('carro velho')

print('---Fim---')

If simplificado, utiliza uma única linha para o if e para o else 
tempo = int(input('quantos anos tem seu carro ?'))

print('carro novo' if tempo <= 3 else 'carro velho')
print('FIM')

nome = str(input('Qual seu nome ?  '))

if nome == 'João':
    print('que nome lindo você tem')
else:
    print('seu nome é tão normal')
print('Bom dia, {}'.format(nome))
--------------------------------------------------------------------------------------------------
n1 = float(input('Digite a sua primeira nota: ' ))
n2 = float(input('Digite a sua segunda nota: '))
m = (n1+n2)/2
print('Parabens' if m >= 6.00 else "estude mais")
if m >= 6.0:
    print('Sua média foi boa! Parabens!')
else:
    print('Sua média foi ruim, estude mais')

2 forma mais simplificada
print('Parabens' if m >= 6.00 else "estude mais")
--------------------------------------------------------------------------------------------------
Exercício Python 028: Escreva um programa que faça o computador "pensar"
import random
from time import sleep
num = random.randint(0, 5)


print('-=-' *20)
print('vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
usuário = float(input('Qual número o computador gerou: '))
print('Processando...')
sleep(2)
if usuário == num:
    print('usuário venceu')
    
else:
    print('Você perdeu, revolução das maquinas')
    print('Ganhei, Eu pensei no {} e não no {}'.format(num, usuário))
--------------------------------------------------------------------------------------------------
Exercício Python 029: 
Velocidade_do_carro = float(input('Qual a velocidade do carro: '))
multa = (Velocidade_do_carro - 80) * 7
if Velocidade_do_carro > 80:
    print('Você foi multado ')
    print('A multa vai custar R$ {:.2f} reais'.format(multa))
else: 
    print('boa viagem')
--------------------------------------------------------------------------------------------------
Exercício Python 030
numero = int(input('Digite um número para saber se ele é PAR ou IMPAR: '))
resultado = numero % 2
if resultado == 0:
    print(' O número {} é PAR'.format(numero))
else:
    print(' O número {} é impar'.format(numero))
--------------------------------------------------------------------------------------------------    
Exercício Python 031
Distância = int(input('Qual a distância da sua viagem :'))

'''if Distância <= 200:
    preço = Distância * 0.5
    print(' O valor da sua viagem de {}KM é RS{}'.format(Distância, preço))
else:
    preço = Distância * 0.45
    print('O valor da sua viagem de {}KM é RS{}'.format(Distância, preço))
''' 
# forma mais simplificada de se fazer 
preço = Distância * 0.50 if Distância <= 200 else Distância * 0.45

print('O preço da sua passagem será de R$ {:.2f}'.format(preço))
--------------------------------------------------------------------------------------------------
Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('Informe um ano:  '))


if ano % 4 == 0:
    print(' O ano {} é um ano BISSEXTO'.format(ano))
    
else:
    print('O ano {} não é um ano bissexto'.format(ano))

--------------------------------------------------------------------------------------------------
Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
from time import sleep

n1 = float(input(' Digite um numero :'))
n2 = float(input('digite o segundo numero:'))
n3 = float(input('Digite o terceiro número: '))

menor = n1

if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
maior = n1

if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

print('PROCESSANDO...')
sleep(2)
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado é {}'.format(maior))
--------------------------------------------------------------------------------------------------
Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
salario = float(input('Informe o valor do seu salário: R$'))

if salario > 1250.00:
    aumento = salario * 0.10 + salario
    print('Seu salário é R${}, recebendo 10% de aumento vai para R${:.2f}'.format(salario, aumento))
else:
    aumento = salario * 0.15 + salario
    print('Seu salário é de R${}, recebendo 15% de aumento vai para R${:.2f}'.format(salario, aumento))

--------------------------------------------------------------------------------------------------,
Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-='*20)
print('ANALISADOR DE TRIÂNGULOS')
print('-='*20)
r1 = float(input('primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('terceiro segmento:' ))

if r1< r2+r3 and r2 < r1+r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar triângulo!')
else:
    print('Os segmentos acima não podem formar triângulo')

"""
