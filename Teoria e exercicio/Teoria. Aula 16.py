"""
Variáveis Compostas
Tuplas
 ----------- Teoria------------
As tuplas são imutáveis!!!! 
posso criar tuplas sem parenteses
================================
lanche = ('suco','pizza','hamburguer', 'Pudim')
print(lanche[:2])
lanche = ('suco','pizza','hamburguer', 'Pudim')
print(lanche[0:2])
lanche = ('suco','pizza','hamburguer', 'Pudim')
print(lanche[1:3])

lanche = ('suco','pizza','hamburguer', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba')
 Resposta = Eu vou comer suco
Eu vou comer pizza
Eu vou comer hamburguer
Eu vou comer Pudim
Comi pra caramba

lanche = ('suco','pizza','hamburguer', 'Pudim')
print(len(lanche))
print('Comi pra caramba')
resposta = O len faz a contagem de quantos itens há na tupla no presente caso, tem 4 itens 
================================================================================================
================================2 formas para o mesmo resultado ================================
                                for comida in lanche:
                                    print(f'Eu vou comer {comida}')
                                print('Comi pra caramba')
                                Resposta ==

                                lanche = ('suco','pizza','hamburguer', 'Pudim')
                                for cont in range(0, len(lanche)):
                                print(f'eu vou comer {lanche[cont]}')

                                Eu vou comer suco
                                Eu vou comer pizza
                                Eu vou comer hamburguer
                                Eu vou comer Pudim
                                Comi pra caramba
================================================================================================
for pos, comida in enumerate(lanche):
  print(f'eu vou comer {comida} na posição {pos}')
ENUMERATE = No enumerate ele me da tanto o dado quanto a posição
eu vou comer suco na posição 0
eu vou comer pizza na posição 1
eu vou comer hamburguer na posição 2
eu vou comer Pudim na posição 3
Comi pra caramba
================================================================================================
 2 formas de fazer 
lanche = ('suco','pizza','hamburguer', 'Pudim')
for cont in range(0, len(lanche)):
  print(f'eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
   print(f'eu vou comer {comida} na posição {pos}')
print('Comi pra caramba')
Resposta eu vou comer suco na posição 0
eu vou comer pizza na posição 1
eu vou comer hamburguer na posição 2
eu vou comer Pudim na posição 3
Comi pra caramba

Destas maneira cito a posição 
================================================================================================
for pos, comida in enumerate(lanche):
   print(f'eu vou comer {comida} na posição {pos}')
print('Comi pra caramba')

lanche = ('suco','pizza','hamburguer', 'Pudim')
for cont in range(0, len(lanche)):
  print(f'eu vou comer {lanche[cont]} na posição {cont}')

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba')
####### Sorted = ordenado
print(sorted(lanche))
================================================================================================
a = (2, 5,4)
b = (5,8,1,2)
c = a + b
print(c)
print(len(c)) = 7
print(c.count(5)) = para contar quantas vezes o número 5 aparece nas tuplas
respota = (2, 5, 4, 5, 8, 1, 2)
print(c.index(2)) = para mostrar a posição do número 2
print(c.index(5,1)) = (5, 8, 1, 2, 2, 5, 4), como há ocorrência do 5 2x  com o (5,1) eu conto a partir da posição 1
pessoa = ('Gustavo', 39, 'M', 99.88) = ('Gustavo', 39, 'M', 99.88)
del(pessoa) # para apagar a tupla da memória 
================================================================================================
print(f'\nO maior valor foi {max(variavel que está sendo trabalhada)}') - para o maior número
print(f'O menor valor foi {min(variavel que está sendo trabalhada)}') - para o menor número

""" 
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
  n = int(input('Digite um número entre 0 e 20:  '))
  if 0 <= n <= 20:
    break
  print('tente novamente. ', end=' ') 
print(f'Você digitou o número {cont[]}') 
    