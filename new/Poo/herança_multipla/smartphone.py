from Poo.herança_multipla.eletronico import *
from Poo.herança_multipla.log import LogMixin



class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome) -> None:
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado: # se eles não estiver ligado, retorna o erro
            info = f' {self._nome} não da para conectar, sem ele ligado!'
            print(info)
            self.log_error(info)
            return
        if self._conectado: # se ele estiver ligado, eu vou checar se eles está conectado 
            error = f' {self._nome} Já está conectado!!!'
            print(error)
            self.log_error(error)
            return
        info = f' {self._nome} Está conectado!!' 
        print(info) #quando ele estiver conectado é infor
        self.log_info(info)
        self._conectado = True #validação se eles está conectado

    def desconectar(self):
        if not self._conectado: # se não está conectado, se eu mandar ele desconectar e ele não estiver ligado retornar erro abaixo ↓
            error = f'{self._nome} Já foi  desconectado!!!.'
            print(error)
            self.log_error(error)
            return
        info = f'{self._nome} foi  desconectado com sucesso'
        print(info)
        self.log_info(info)
        self._conectado = False