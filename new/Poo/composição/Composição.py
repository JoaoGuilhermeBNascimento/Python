class Cliente:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        self.endereços = []

    def inserir_endereço(self, cidade, estado):
        self.endereços.append(Endereço(cidade, estado))
    
    def lista_endereços(self):
        for endereços in self.endereços:
            print(endereços.cidade, endereços.estado)

    def __del__(self):
        print(f'{self.nome} foi apagado!!!')

class Endereço:
    def __init__(self, cidade, estado) -> None:
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade}/{self.estado} foi apagado')