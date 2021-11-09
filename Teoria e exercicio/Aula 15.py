"""
cont = 1 
while cont <= 10:
    print(cont, '→', end='')
    cont += 1
print('acabou')
 Resultado 1 →2 →3 →4 →5 →6 →7 →8 →9 →10 →acabou

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n

#print('A soma vale {}'.format(s))
print(f'A soma vale {s}')
    

nome = ' Jose'
idade = 33
salario = 987.35
print(f'O {nome:-^20} tem {idade} anos e ganha R${salario:.2f}.')
#print(f'O {nome} tem {idade} anos')
==============================================
Desafio 66
==============================================
n = s = cont = 0 
while True:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'Foram digitados {cont} e a soma deles é {s}')
==============================================
Desafio 067
==============================================
#######Minha versao###
while True:
    n = int(input('Quer ver a tabuada de qual valor:  '))
    if n < 0:
        break
    print('~~'*20)
    for c in range (1,11):
        print(f'{n} x {c} = {n*c}')
    print('~~'*20)
print('Programa de Tabuada ENCERRADO. Até logo')
==============================================
Desafio 068
==============================================
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

==============================================
Desafio 69
==============================================
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
    
==============================================
Desafio 71
==============================================
print('{:-^40}'.format('Caixa Eletronico!'))

valor = int(input('Qual valor a ser sacado:  '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1

    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R$ {céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
            totcéd = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao BanCo Nubank')
==============================================
"""
