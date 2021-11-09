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

print('{:=^40}'.format('Lojas Nascimento'))
preço = int(input('Qual o valor do produto: R$  '))
print('=='*20)
print(" Escolha uma opção de pagamento:
[1] À vista DINHEIRO/CHEQUE: 10% de desconto
[2] À vista no cartão: 5% de desconto
[3] Em até 2x no cartão: preço normal
[4] 3x ou mais no cartão: 20% de Juros"")
opção = int(input('Escolhe uma opção de pagamento:  '))

if opção == 1:
    desconto = preço - (preço * 0.1)
    print('valor sem desconto R${},para  pagamentos à vista recebe 10% de desconto e o valor fica {} '.format(preço,desconto))
elif opção == 2:
    desconto = preço - (preço*0.05)
    print('Valor sem desconto R${}, para pagamento à vista no cartão, com 5% de desconto fica R${} '.format(preço,desconto))
elif opção ==3:
    print('Para pagamentos em até 2x no cartão, o preço fica R${}'.format(preço))
elif opção ==4:
    n = int(input('Quantas parcelas deseja dividir: '))
    juros = preço +(preço *0.2) # 20/100
    r = (juros/n)
    print('Para pagamento em 3x ou mais no cartão, será cobrado um juros de 20%.')
    print('O valor final é R${} , dividido em {} vezes,fica R${} durante {} meses'.format(juros, n,r,n))


from random import randint,randrange
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

print("" Escolha uma opção:
[0] PEDRA
[1] PAPEL
[2] TESOURA"")
jogador = int(input('Escolha uma opção: '))
print('Computador jogou {}'.format(itens[computador]))
print('=-'*10)
print('Jogador jogou {}'.format(itens[jogador]))

if computador ==0:
    if jogador ==0:
        print('EMPATE')
    elif jogador ==1:
        print('JOGADOR VENCEU')
    elif jogador ==2:
        print('Jogador PERDEU')
elif computador ==1:
    if jogador ==0:
        print('Jogador PERDEU')
    elif jogador ==1:
        print('EMPATE')
    elif jogador ==2:
        print('Jogador VENCEU')
elif computador ==2:
    if jogador ==0:
        print('Jogador VENCEU')
    elif jogador ==1:
        print('Jogador PERDEU')
    elif jogador ==2:
        print('EMPATE')

for c in range (0,6):
    print ('oi')
print('Fim')

for c in range (0, 7, 2):
    print (c)
print('Fim')

i = int(input('ínicio: '))
f = int(input('Fim: '))
p = int(input('Passo:'))
for c in range(i, f+1, p):
    print(c)
print('Fim')

for  c in range(6,0, -1): # esse -1 vai significar qual é a iteração, o que irá acontecer no final do laço, que irá começar no 6 e vai tirar 1 
    print(c)
print('FIM')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))
from time import sleep
print('A contagem regressiva para estouro de fogos começa ')
for c in range (10,-1, -1):
    sleep(1)
    print(c) 
    
print('FIM ')

for c in range (2, 51, 2):
    print(c, end=' ')
    
print('FIM')

s = 0
cont = 0
for c in range (1 , 501, 2):
    if c % 3 ==0:
        print(c, end=' ')
        cont += 1
        s += c

print(' A soma de todos os {} solicitados é {}'.format(cont, s))
      
    num = int(input('Qual a tabuada desejada: '))

for n in range (1, 11):
    print( '{} X {} = {}'.format(num, n,num*n) )
print('Fim')

s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}º valor: '.format(c)))
    if n % 2 == 0:
        s += n
        cont += 1
print('Você informou {} numeros e a soma dos números pares foi {}'.format(cont ,s))
print('FIm')

i = int(input('ínicio: '))
f = int(input('Fim: '))
p = int(input('Passo:'))
for c in range(i, f+1, p):
    p = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão desejada: '))
decimo_termo = p + (10-1) *r
for c in range(p, decimo_termo , r):
    print('{}'.format(c), end=' → ')
print('FIM')
n = int(input('Digite um número inteiro: '))
tot = 0

for c in range (1, n+1):
    if n % c == 0:
        print('\33[33m', end=' ')
        tot += 1
    else:
        print('\33[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(n, tot))
if tot == 2:
    print('É um número PRIMO')
else:
    print('não é PRIMO')
    from datetime import date
atual = date.today().year
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
totmulher20 = 0
for c in range (1,4):
    print('---------{}ª Pessoa-----------'.format(c))
    nome = str(input('Qual o nome da {}ª pessoa : '.format(c)))
    idade = int(input('Qual a idade da {}ª pessoa: '.format(c)))
    sexo = str(input('Qual o sexo da {}ª pessoa [M/F]'.format(c))).upper()
    soma_idade+= idade
    if c == 1 and sexo == 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 +=1
media_idade = soma_idade/4
print('A média de idade do grupo é {}'.format(soma_idade))  
print('O homem mais velho tem {} e seu nome é {}'.format(idade,nome_velho))
print('Tem {} mulheres com menos de 20 anos'.format(totmulher20))
========================================================================================
c = 1 
while c < 10:
    print(c)
    c +=1 # Quando ele retornar eu quero que some mais +1
print('FIM')

Situação que enquanto eu quiser continuar ele irá voltar para o laço 
r = 'S'
while r == 'S':
    n = int(input('Digite um valor:  '))
    r = str(input('Quer continuar [S/N]: ')).upper()
print('FIM')
# se eu não souber quantos valores são, posso colocar uma condição de parada
n = 1
while n != 0:
    n = int(input('Digite um valor:  '))
   
print('FIM')
 
 n = 1 
par = impar = 0
while n != 0:
    n = int(input('Digite um valor:  '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar +=1
print('Você digitou {} números pares e {} números impares!'.format(par, impar))
========================================================================================
Exerciocio 57
========================================================================================
sexo = str(input('Qual seu sexo [M/F]: ')) .strip() .upper() [0]
while sexo not in 'M' or 'F':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo')).strip() .upper() [0]
    if sexo == 'M':
        print('Sexo Masculino')
        print('Sexo cadastrado com sucesso!!')
    elif sexo == 'F':
        print('Sexo Feminino!')
        print('Sexo cadastrado com sucesso!!')
    
print('FIM')
sexo = str(input('Qual seu sexo [M/F]: ')) .strip() .upper() [0]
while sexo not in 'M' or 'F':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo:  ')).strip() .upper() [0]
    if sexo == 'M':
        print('Sexo Masculino')
        print('Sexo cadastrado com sucesso!!')
    elif sexo == 'F':
        print('Sexo Feminino!')
        print('Sexo cadastrado com sucesso!!')
    
print('FIM')
from random import randint
    
s = 0
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10')
print('=='*20)
print('será que você consegue adivinhar qual foi ?')
print('=='*20)
acertou = False
while not acertou:
    jogador = int(input('qual é o seu palpite: '))
    print('=='*20)
    s += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print(' Mais..')
        elif jogador > computador:
            print('Menos..')
print('Acertou com {} tentavias. parábens!'.format(s))

Minha forma
from random import randint
s = 0
itens = [0, 10]
computador = randint(0,10)
jogador = int(input('tente acertar o número do computador entre 0 e 10: '))
while not  jogador == computador:
    jogador = int(input('Você errou! \n tente novamente! '))
    if jogador == computador:
        print('Você venceu!')
    s +=1
n1 = int(input('Informe o 1º valor: '))
n2 = int(input('Informe o 2º valor: '))
opçao = 0


while opçao != 5:
    print(" Escolha uma opção:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
    opçao = int(input('Escolha uma opção do Menu: '))
    print('=='*20)
    if opçao == 1:    
        print('A soma de {} + {} = {}'.format(n1,n2,n1+n2))
        print('=-='*20)
    elif opçao ==2:
        print('A multiplicação de {} X {} = {}'.format(n1,n2,n1*n2))   
        print('=-='*20)
    elif opçao ==3:
        if n1 > n2:
            print('O valor {} é maior que {}'.format(n1,n2))
            print('=-='*20)
        elif n2 > n1:
            print('O valor {} é maior que {}'.format(n2,n1))
            print('=-='*20)
    elif opçao ==4:
        n1 = int(input('Informe o 1º valor: '))
        n2 = int(input('Informe o 2º valor: '))
        print('=-='*20)
    elif opçao ==5:
        print('Obrigado por usar nosso programa')
        print('=-='*20)
    else:
        print('opção inválida!!\n Tente novamente!')

        from math import factorial


n = int(input('Digite um número para cálcular seu fatorial:  '))
c = n
f = 1
print('Calculando {}!'.format(n))
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print('{}'.format(f))
========================================================================================
from math import factorial
n = int(input('Informe um número: '))
for c in range (n,0,-1):
    print(c, end=' ')
    print(' x ' if c > 1 else ' = ',end=' ')
print(factorial(n))

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
========================================================================================
print('=-='*30)
n = int(input('quantos termos você quer mostrar ?  '))
print('=-='*30)
t1 = 0 
t2 = 1
print('=-='*30)
print('{} → {}'.format(t1, t2), end=' ')
cont = 3 
while cont <= n:
    t3 = t1+t2
    print('→ {}'.format(t3), end=' ')
    t1 = t2
    t2 = t3
    cont +=1

print('FIM')
print('~'*30)

========================================================================================
n = 0
s = 0
cont = 0
n = int(input('Digite um número inteiro: ')) # colocar o input fora do while 
while n != 999:
    s += n
    cont += 1
    n = int(input('Digite um número inteiro: ')) # é dentro do while para desconsiderar o flag, que no caso é o 999.
print ('Você digitou {} números e a soma entre eles foi {}.'.format(cont,s))
========================================================================================
#Não está completo
print ('~'*20)
n = int(input('Informe um valor inteiro: '))
cont = 0
soma = 0
mais = 1
while mais != 0:
    while n != 0:  
        soma += n
        cont += 1
        print ('~'*20)
        n = int(input('Informe um valor inteiro: '))
    media = soma/cont
    print('Foi informado {} numeros \nA soma é {} !\n A média entre todos é {} '.format(cont,soma, media))
    mais = int(input('Você quer continuar a digitar valores ? Se Sim Digite os valores se não, digite 0! '))
print('Fim do programa')
========================================================================================
resp = 'S'
media = soma = quant = maior = menor = 0
# soma = quant = media = 0 Pode ser feito dessa forma
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    if quant ==1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n   
    resp = str(input('Quer continuar ? [S/N] ')).strip()[0] .upper()
media = soma/quant
print('Você digitou {} números é a média foi {}'.format(quant,media))
print('O número {} é o maior e o número {} é o menor '.format(maior, menor))
========================================================================================

from random import randint

cont = par = impar = 0
soma = 0
print('=-='*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
while True:  
    
    n = int(input('Digite um valor: '))
    computador = randint(0,10)
    soma = n + computador
    jogador = ' '
    while jogador not in 'PpIi':
        jogador =  str(input('Par ou Ímpar [P/I]:  ')).upper() .strip()[0]
    print (f'Você jogou {n} e o computador {computador}.Total de {soma}')
    if jogador  == 'I':
        if soma %2 != 0:
            impar += 1
            cont += 1
            print('Jogador Venceu')
            
        else:
            print('COMPUTADOR VENCEU. Tente novamente')
            break
    if jogador == 'P':
        if soma % 2 ==0:
            par += 1
            cont += 1
            print('Jogador venceu')
            
        else: 
            print('Computador Venceu. Tente novamente')
            break
    print('Vamos jogar novamente... = D')

print(f'GAME OVER!! Você venceu {cont} vezes')
"""

cont = totalM = totalH = 0
resposta = 'S'

print('=-='*20)

while resposta in 'Ss':
    print('=='*20)
    print('Cadastre uma pessoa')
    print('=='*20)
    idade = int(input('Qual a sua idade ? '))
    sexo = ' '
    while sexo not in 'HM':
        sexo = str(input('Qual seu sexo [H/M]:  ')).upper() .strip()[0]

        resposta = ' '
        while resposta not in 'SN':
            resposta = str(input('Quer continuar [S/N]: ')).upper() .strip()[0]
            if resposta == 'Nn':
                break

        if idade > 18:
            cont += 1
        if sexo == 'M' and idade < 20:
            totalM += 1
        if sexo == 'H':
            totalH += 1 
        
print(f'Foram contabilizados {cont} pessoas com mais de 18 anos.')
print('=-='*20)
print(f'Foram contabilizados {totalH} homens.')
print('=-='*20)
print(f'Foram contabilizados {totalM} mulheres com menos de 20 anos.')
print('Programa encerrado')