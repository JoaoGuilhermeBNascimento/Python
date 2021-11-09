"""
Funções - Parte 1 
def soma(a,b):
    s = a + b
    print(s)


soma(4,5)
soma(8,9)
soma(2,1)
 =========================================
def soma(a,b):
    print(f'A = {a} e B = {b}')
    soma = a + b
    print(f'A soma A + B = {soma}')
    print('-='*30)
    

soma(b=4,a=6)

=========================================
def lin():
    print('============')


lin()
print('Sistema')
lin()
print('cadastro de funcionarios')
lin()
=========================================
def titulo(txt):
    print('-'*30) 
    print(txt)
    print('-'*30)


titulo('Sistema')

titulo('cadastro de funcionarios')
=========================================
#EMPACOTANDO PARAMETROS
def contador(*num): #* asterisco significa desempacotar, tirar tudo e jogar dentro de num, a variavel 
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
=========================================
# TRABALHANDO COM LISTAS AO INVES DE TUPLAS
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos]*=2
        pos +=1

valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
=========================================
def soma(* valores):
    s = 0
    for num in valores:
        s += num
        print(f'Somando os valores {valores} temos {s} ')
soma(5, 2)
soma(2, 9, 4)
"""
from time import sleep
num = 0
print('=-'*30)
print('contagem de 1 até 10 de 1 em 1')
for num in range(1,11):
        
    print(f'{num}',end=' ')
        
print('FIM')
print('=-'*30)
print('Contagem de 10 até 0 de 2 em 2')
for num in range(10,1,-2):
        print(f'{num}',end=' ' )
print('FIM')
print('=-'*30)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('FIM: '))
passo = int(input('Passo: '))
for num in range(inicio,fim,passo):
    print(f'{num}', end=' ')