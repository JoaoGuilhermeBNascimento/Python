class escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property # getter
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta

class Caneta:
    def __init__(self, marca):
        self.__marca = marca


    def escrever(self):
        print('Caneta está escrevendo...')
        

    @property
    def marca(self):
        return self.__marca


class MaquinaDeEscrever:
    def __init__(self, label) -> None:
        self.__label = label

    def escrever(self, label):
        print(f'A maquina de escrever {label} está datilografando...')

    @property
    def label(self):
        return self.__label