from Poo.herança_multipla.eletronico import *
from Poo.herança_multipla.log import LogMixin
class Smartphone(Eletronico):
    def __init__(self, nome) -> None:
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado: # se eles não estiver ligado, retorna o erro
            print(f' {self._nome} não da para conectar, sem ele ligado!')
            return
        if self._conectado: # se ele estiver ligado, eu vou checar se eles está conectado 
            print(f' {self._nome} Já está conectado!!!')
            return
        print(f' {self._nome} Está conectado!!')
        self._conectado = True #validação se eles está conectado

    def desconectar(self):
        if not self._conectado: # se não está conectado, se eu mandar ele desconectar e ele não estiver ligado retornar erro abaixo ↓
            print(f'{self._nome} não está CONECTADO.')
            return
        self._conectado = False