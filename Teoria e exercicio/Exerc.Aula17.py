"""
Desafio 78
=======================================================
valores = []
for cont in range(1,6):
    valores.append(int(input(f'Digite o {cont}º valor →  ')))
    
for c, v in enumerate(valores):
    print(f'Na  posição {c+1} encontrei o valor {v} ')
print(valores,'\n', end=' ')
print(f'O maior foi {max(valores)} ')
print(f'O menor foi {min(valores)}')
print(sorted(valores))
=======================================================
valores = []

max = 0 
min = 0 
for c in range(0,5):
    valores.append(int(input(f'Digite o valor na poisção {c} 5→  ')))
    if c ==0:
        max = min = valores[c]
    else:
        if valores[c] > max:
            max = valores[c]
        if valores[c] < min:
            min = valores[c]
print('=-'*30)
print(f'você digitou os valores {valores}')
print(f'O maior valor digitado foi {max} nas posições', end= ' ')
for i, v in enumerate(valores):
    if v == max:
        print(f'{i}....', end=' ')
print()
print(f'O menor valor digitado foi {min} nas posiçõesm', end=' ')
for i, v in enumerate(valores):
    if v == min:
        print(f'{min}....',end=' ')
print()
=======================================================
Desafio 79
=======================================================
lista = []

while True:

    n = (int(input('Digite um valor númerico →  ')))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = str(input('Deseja continuar ? [S/N] ')).upper() .strip()[0]
    if resp in 'N':
        break
    
    
print(sorted(lista))
=======================================================
Desafio 80 
=======================================================
lista = []
for c in range (0,5):
    n = int(input(f'Digite o {c} valor → '))
    if c == 0 or n > lista[-1]: # n > lista[-1] para pegar o último elemento
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos +=1
print('=-'*30)
print(f'Os valores digitados em ordem foram {lista}')
=======================================================
Desafio 81
======================================================
lista = []
cont = 0
while True:
    lista.append(int(input('Digite um valor → → ')))
    cont +=1
    
    resp = str(input('Você quer continuar  ? [S/N]  ')).upper().strip()[0]
    if resp in 'Nn':
        print('programa finalizado')
        break
if 5 in lista:
    print('O valor 5 foi digitado')
else:
    print('O valor 5 não está na lista ')
print('-='*30)
print(f'Foram digitados {cont} números')
#print(f'foram digitados {len(lista)} elementos)
lista.sort(reverse=True)
print(lista)
======================================================
Desafio 82
======================================================
lista = []
par = []
impar = []

while True:
    n = int(input('Digite um valor → '))
    lista.append(n)
    
    resp = str(input('Quer continuar ? [S/N] → ')) .upper() .strip()[0]
    if resp in 'Nn':
        print('Fim do programa')
        break
for i, v in enumerate(lista):
    if v % 2 ==0:
        par.append(v)
    elif v % 2 ==1:
        impar.append(v)
        
""" 
expr = str(input('Digite a expressão '))

pilha = list()
for simb in expr:
    if simb =='(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) ==0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está errada')

