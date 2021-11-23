# agregação e composição
# uma classe usa outra classe como parte de si e essa classe precisa da outra classe.
class CarrinhoDeCompras:
    def __init__(self) -> None:
        self.produtos = []

    def inserir_produto(self,produto):
        self.produtos.append(produto)

    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total
class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor 
        