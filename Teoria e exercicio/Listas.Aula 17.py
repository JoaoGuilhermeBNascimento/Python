"""
Para utilizar lista ao inves de TUPLAS é só utilizar colchetes
Ex.: 
lista = ['Carro', 'Moto']
============================================================================
lanche.append[cookie] = adiciona um elemento a lista
============================================================================
lanche.insert(0,'banana')= adiciona o item conforme a posição descrita
============================================================================
PARA APAGAR ELEMENTOS UTILIZA OS COMANDOS 
del lanche[3]
ou
lanche.pop(3) se colocar lanche.pop() --> elimina o último elemento
ou
lanche.remove('pizza')
============================================================================
Testes
lanche = ['hamburguer', 'cerveja','pizza','pudim']
lanche [3] = 'stroggnoff'
lanche.insert(6,'cookie')
lanche.pop(3)
lanche.remove('pizza')
print(lanche)
============================================================================
Listas com ranges

valores = list(range(4,11))
print(valores)
valores = [8,2,5,4,9,3,0]

valores.sort()  = [0, 2, 3, 4, 5, 8, 9]
valores.sort(reverse=True) = para ordenar os valores na ordem reversa = [9, 8, 5, 4, 3, 2, 0]

len(valores) = quantos elementos tem na lista
print(valores)
============================================================================
num = [2, 5, 9,1]
num[2] = 3 # para transforma o número da posição 2( que é o 9 ) em 3 
num.append(7) # para adicionar número ao elemento utilizar append
num.sort(reverse=True) # sort para colocar em ordem. Se utilizar o reverse=True ele inverte a ordem
num.insert(2, 0) # na posição 2 inserir o zero
num.pop(2) # elimina o último elemento, colocando uma posição dentro do parentese ele elimina o número daquela posição
print(num)
============================================================================
num = [2, 5, 9,1]
num[2] = 3 # para transforma o número da posição 2( que é o 9 ) em 3 
num.append(7) # para adicionar número ao elemento utilizar append
num.sort(reverse=True) # sort para colocar em ordem. Se utilizar o reverse=True ele inverte a ordem
num.insert(2, 2) 
if 5 in num:
    num.remove(5) # o remove procura do inicio da lista a primeira ocorrência do valor que foi mandado eliminar
else:
    print('Não achei o numero 5')
print(num)
print(f'Essa lista tem {len(num)} elementos')
============================================================================,
POSSO CRIAR LISTA DE 2 FORMAS
valores = []
ou
valores = list()

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}....', end= ' ')
RESPOSTA 5.... 9.... 4.... 
============================================================================,
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista')

Resposta = 
Na posição 0 encontrei o valor 5
Na posição 1 encontrei o valor 9
Na posição 2 encontrei o valor 4
Cheguei ao final da lista

============================================================================,
valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista')
APÓS A DIGITAÇÃO DE 4 VALORES NO INPUT, FOI DADO O NOME DENTRO DA POSIÇÃO E DA LISTA
RESPOSTA = Na posição 0 encontrei o valor 4
Na posição 1 encontrei o valor 4
Na posição 2 encontrei o valor 6
Na posição 3 encontrei o valor 3
Na posição 4 encontrei o valor 2
Cheguei ao final da lista
============================================================================
===================================================
valores = []
for cont in range (0,5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}! ')
    Digite um valor: 4

Digite um valor: 8
Digite um valor: 9
Digite um valor: 1
Digite um valor: 3
Na posição 0 encontrei o valor 4! 
Na posição 1 encontrei o valor 8!
Na posição 2 encontrei o valor 9!
Na posição 3 encontrei o valor 1!
Na posição 4 encontrei o valor 3
===================================================
a = [2,3,4,7]
b = a # a partir do momento que eu igualo uma lista com a outra, o python cria uma ligação entre elas, adicionando o valor de b[2] = 8 em a e b
b[2] = 8
print(f'Lista A:{a}')

print(f'Lista B: {b}')
resposta = 
Lista A:[2, 3, 8, 7]
Lista B: [2, 3, 8, 7]
============================================================================
a = [2,3,4,7]
b = a[:] # desta forma cria uma copia de A dentro do b
b[2] = 8 # tirando a ligação do B com A 
print(f'Lista A:{a}')

print(f'Lista B: {b}')
"""
valores = []
for cont in range (1,6):
    valores.append(int(input(f'Digite o {cont}º valor:')))
for c , v in enumerate(valores):
    print(f'A posição ')