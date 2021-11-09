"""

def area(larg, comp):
    a = larg * comp
    print('-'*20)
    print(f'A área de um terreno {larg} X {comp} é de {a}m²')
    print('-'*20)


print('Controle de Terrenos')
print('-'*20)
l = float(input('Largura (m): '))
print('-'*20)
c = float(input('COMPRIMENTO (m): '))
area(l, c)
=============================================
Desafio 97
=============================================
def escreva(txt):
    tam = len(txt) # utilizar está variavel para definir o tamanho das linhas que acompanham o texto
    print('~~'*tam)
    print(f'  {txt}')
    print('~~'*tam)


escreva('Joao Guilherme')
=============================================
Desafio 98
=============================================
from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p ==0:
        p = 1
    print('=-'*30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    #sleep(2.5)

    
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
           # sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >=f:
            print(f'{cont}',end=' ', flush=True)
            #sleep(0.5)
            cont -=p
        print('FIM!')
       
    


contador(1,10,1)
contador(10,0,2)
print('=-'*30)
print('Agora é sua vez de personalizar a contagem! ')
inicio = int(input('Início:    '))
fim = int(input('FIM:        '))
passo = int(input('Passo:    '))
contador(inicio,fim,passo)
=============================================
Desafio 99
=============================================
def maior(* num):
    cont = maior = 0
    print('-='*30)
    print('\nAnanlisando os valores informados....')

    for valor in num:
        print(f'{valor}', end=' ')
        if cont ==0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont +=1
    print(f'Foram informado {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 8, 0)
maior(1,2)
maior(6)
maior()

"""
