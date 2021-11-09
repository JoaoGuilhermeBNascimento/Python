import moeda


n = float (input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))} ')
print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n)} ')
print(f'Aumentando 10% de {moeda.moeda(n)}, temos {moeda.moeda(moeda.aumento(n))} ')
print(f'Reduzindo 13% de {moeda.moeda(n)}, temos {moeda.moeda(moeda.diminuir(n))}')