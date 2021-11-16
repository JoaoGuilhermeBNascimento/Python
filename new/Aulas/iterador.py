# iteradores serve para consumir os valores deles

nome = ' João Guilherme'
iterador = iter(nome)
gerador = (letra for letra in nome)
""" try:
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
except:
    pass

for valor in iterador:
    print(valor) """

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print('--')
for letra in gerador:
    print(letra)