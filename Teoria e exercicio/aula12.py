###  CONDIÇÕES ANINHADAS###
"""
nome = str(input('Qual é seu nome? '))
if nome == ' Joao':
    print('Que nome bonito')
elif nome == 'Pedro' or nome == ' Maria' or nome == 'Paulo' :
    print('seu nome é bem normal no brasil')
elif nome in 'Ana Cláudia Jéssica':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia {}'.format(nome))

códigos para estilo
0 - nada
1 = em negrito - bold
4 = Underline = sublinhado
7 - Inverter as configurações - negative 

as opções de cores é do 30 a 37 
30 - branca 31 - vermelha - 32 verde - 33 - amarela 34 - azul 35 - roxo - 36 azul bb - 37 - cinza  ( CORES DE TEXTO)
40 '' '' 41 42 43 44 45 46 47 - mesmas  corse do text mas agora no background 
para letra preta e fundo branco usamos \33[7:30m
  \033[0;33;44m
  ------------------------------------------------------------------
Exercício 36
from time import sleep
valor_da_casa = float(input('Qual o valor da casa que o senhor(a) deseja ?'))
print('=-'*20)
salario = float(input('Qual o seu salário ?'))
print('=-'*20)
pagamento_em_anos = float(input('Em quantos anos deseja pagar ?'))
print('Processando...')
sleep(2)

excedente = salario * 0.3
parcela = valor_da_casa/ (pagamento_em_anos*12)

if parcela > excedente:
    print('A parcela fica em {:.2f} e excede 30% do seu salário, emprestimo \33[1;31mnegado!!!\33[m'.format(parcela))
else:
    print('Credito aprovado!! O valor da sua parcela será de \33[1;31mR${:.2f} por mês durante {}anos'.format(parcela, pagamento_em_anos))
    ------------------------------------------------------------------
    Exercício 37 
 num = int(input(' Informe um número inteiro: '))
print ("Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL"""
""""
opção = int(input('Sua opção:  '))

if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num,oct(num)))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)))
else:
    print('Opção inválida, tente novamente.') 

------------------------------------------------------------------
Exercício 38
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número:  '))

if n1>n2:
    print('O Primeiro valor {} é Maior '.format(n1))
elif n2>n1:
    print('O segundo valor {} é maior'.format(n2))
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais')
else:
    print('valores inválido')
ano = int(input('Qual seu ano de nascimento ? '))

from datetime import date
atual = date.today().year
if ano > 2003:
    idade = 2021 - ano
    faltam = 18 - idade
    print('Você nasceu em {} tem {} em 2021'.format(ano, idade))
    print(' Ainda faltam {} anos para o alistamento '.format(faltam))
elif ano == 2003:
    idade = 2021 - ano
    print('Você tem {} anos, já está na hora de se alistar'.format(idade))
elif ano < 2003:
    idade = 2021 - ano
    passou = idade - 18
    print('Quem nasceu em {} tem {} em 2021'.format(ano, idade))
    print('Você deveria ter se alistado há {} anos'.format(passou))

Exércicio 42
from time import sleep
print('-='*20)
print('Analisador de triangulos')
sleep(1)
print('-='*20)
r1 = float(input('primeiro segmento: '))
r2 = float(input('segundo segmento:  '))
r3 = float(input('terceiro segmento:  '))
if  r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print("os segmentos acima podem formar um triângulo.")

if  r1 == r2 == r3:
    print('Esté triango tem todos os segmentos iguais, é um triangulo EQUILATERO')
elif r1 == r2 or r2 == r3 or r1 == r3:
    print('Esté é um triangulo ISÓSCELES, tem dois lados iguais.')
elif r1 != r2 or r2 != r3 or r3 != r1:
    print('Esté é um triangulo ESCALENO, todos os lados diferentes.')

else:
    print('Opção inválida')
Exercício Python 043 - IMC
peso = float(input('Qual o seu peso em kilogramas ?  '))
altura = float(input('Qual sua altura ? '))
imc = peso/altura**2

if imc < 18.5:
    print('Seu IMC é {:.1f}.Você está abaixo do peso!'.format(imc))
elif imc < 25:
    print('Seu IMC é {:.1f}.Você está no peso ideal.'.format(imc))
elif imc < 30:
    print('Seu IMC é {:.1f}. Você está em sobrepeso!!'.format(imc))
elif imc < 40:
    print('Seu IMC é {:.1f}. Voce está obeso.'.format(imc))
else: 
    print('Seu IMC é {:.1f}. Você está com obesidade mórbida.'.format(imc))
Exercício 44

    from time import sleep
valor = float(input('Informe o valor do produto: '))
pagamento = float(input("CONDIÇÕES DE PAGAMENTO
[1] À VISTA/CHEQUE
[2] À VISTA NO CARTÃO
[3] EM ATÉ 2X NO CARTÃO
[4] 3X OU MAIS NO CARTÃO
ESCOLHA UMA OPÇÃO: 
if pagamento == 1:
    desconto =  valor - (valor * 0.10) 
    print('Para pagamentos à vista dinheiro/cheque você recebe 10% de desconto' )
    print(' O valor do seu produto com desconto é {}'.format(desconto))
elif pagamento == 2:
    desconto = valor - (valor*0.05)
    print('Para pagamentos à vista no cartão, você recebe 5% de desconto')
    print('O valor do seu produto com desconto é {}'.format(desconto))
elif pagamento == 3:
    parcelas = valor/2
    print('Para pagamentos em 2x no cartão mantém o preço normal.')
    print('O valor do seu produto dividido em 2x de {}'.format(parcelas))
elif pagamento == 4:
    juros = (valor*0.2) + valor
    parcelas = float(input('Informe em quantas deseja dividir: '))
    resultado = juros / parcelas
    print('Para pagamentos em 3x ou mais no cartão, incide 20% de JUROS')
    print('O valor do seu produto para dividir em 3x fica em {}'.format(juros))
    print('Dividindo em {}, fica {} de R${}'.format(parcelas, parcelas, resultado))
    import random
itens = ('PEDRA','PAPEL','TESOURA')
computador = random.randint(0,2)
print('O computador escolheu {}'.format(computador))

print("Escolha;
[0] PEDRA
[1] PAPEL
[2] TESOURA"")
jogador = int(input('Qual é a sua jogada ? '))
print('=-'*20)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('=-'*20)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador VENCEU')
    elif jogador == 2:
        print('Jogador PERDEU')
elif computador == 1:
    if jogador == 0:
        print('Jogador PERDEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador VENCEU')
elif computador == 2:
    if jogador == 0:
        print('Jogador Venceu')
    elif jogador == 1: 
        print('Jogador perdeu')
    elif jogador == 2:
        print('EMPATE')
else:
    print('Opção inválida')
    import math
from typing import BinaryIO
numero = int(input('Informe um número inteiro: '))
print("" Escolha qual será a base da conversão desejada: 
[1] BINÁRIO
[2] Octal
[3] Hexadecimal
 "")
opçao = int(input('Sua opção :  '))
if opçao == 1:
    print(' {} convertido para Binário é {}'.format(numero,bin(numero)[2:]))
elif opçao ==2:
    print('{} convertido para Octal é igual a {}'.format(numero,oct(numero)[2:]))
elif opçao==3:
    print('{} convertido para Hexadecimal é {}'.format(numero,hex(numero)[2:]))
else:
    print('opção invalida, tente novamente')
n1 = int(input('Informe um número: '))
n2 = int(input('Informe o segundo número: '))

if n1 > n2:
    print('O primeiro valor {} é Maior que {}'.format(n1,n2))
elif n2 > n1:
    print('O segundo  valor {} é MAIOR que o {}'.format(n2,n1))
elif n1 == n2:
    print('Não existe valor maior, {} e {}, são IGUAIS'.format(n1,n2))
   
    from datetime import date

nascimento = int(input('Informe seu ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento
if idade < 18:
    falta = 18 - idade
    print('Sua idade é {}, ainda falta {} anos para se alistar!'.format(idade,falta))
elif idade == 18:
    print('Sua idade é {},está na hora de se alistar no exercito Brasileiro!'.format(idade))
elif idade > 18:
    passou = idade - 18
    print('Sua idade é {},você passou do prazo de alistamento {} anos, procura a junta militar da sua cidade'.format(idade,passou))

from datetime import date
atual = date.today().year
nascimento = int(input('Informe seu ano de nascimento: '))
idade = atual - nascimento

if idade <= 9:
    print('você tem {} anos, sua categoria é MIRIM'.format(idade))
elif idade <= 14:
    print('Você tem {} anos, sua categoria é INFANTIL'.format(idade))
elif idade < 19:
    print('Você tem {} anos, sua categoria é JUNIOR'.format(idade))
elif idade < 20:
    print('Você tem {} anos, sua categoria é SÊNIOR'.format(idade))
else:
    print('você tem {} anos, sua categoria é MASTER'.format(idade))

""" 
peso = float(input('Qual o seu peso em Kilogramas: '))
altura = float(input('Qual a sua altura em metros: '))

imc = peso/(altura**2)

if imc < 18.5:
    print('Seu IMC é {}, você está abaixo do peso'.format(imc))
elif imc < 25:
    print('Seu IMC é {}, você está no peso ideal.'.format(imc))
elif imc < 30:
    print('Seu IMC é {}, você está em sobrepeso'.format(imc))
elif imc < 40:
    print('Seu IMC é {}, você está obeso '.format(imc))
elif imc > 40:
    print('seu IMC é {}, Você está com obesidade morbida'.format(imc))


