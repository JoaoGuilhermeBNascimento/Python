from abc import ABC, abstractmethod
# abc = abstratct class

class Conta(ABC):# ela herda de abc pois é uma classe abstrata
    def __init__(self, agencia, conta, saldo) -> None:
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia (self):
        return self._agencia
    
    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        # isinstance, estou checando se não for  uma instância inteira ou flutuante
        if not isinstance(valor, (int, float)):
            raise ValueError("Saldo precisar ser númerico ( int ou float)")
            #raise, levanta uma exceção, caso o número informado não seja int ou float
        self._saldo = valor

    def depositar(self, valor):
        if not isinstance (valor, (int, float)):
            raise ValueError("Valor do deposito precisa ser númerico")
            return
        self._saldo += valor
        self.detalhes()
    def detalhes(self):
        print(f'Agência: {self.agencia}', end=' ')
        print(f'conta: {self.conta}', end=' ')
        print(f'Saldo: {self.saldo}')


    @abstractmethod 
    def sacar(self,valor):
        pass

            

