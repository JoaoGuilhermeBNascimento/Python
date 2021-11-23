# agregação e composição
from Poo.Agregação.classes import *

carrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta', 50)
p2 = Produto('iphone', 10000)
p3 = Produto('caneca', 20)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)

carrinho.lista_produto()
print(carrinho.soma_total())