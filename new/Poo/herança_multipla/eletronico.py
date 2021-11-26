from Poo.herança_multipla.log import LogMixin


class Eletronico:
    def __init__(self, nome,) -> None:
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if  self._ligado:
            error = f' {self._nome} Já está ligado!'
            
            self.log_error(error)
            return
        print(f' {self._nome} ligado!!')
        
        if not self._ligado:
            info = f' {self._nome} ligando...'
            self.log_info(info)
            
        self._ligado = True

    def desligar(self):
        if not self._ligado:
            error = f'{self._nome}, não da para desligar, pois já está desligado'
            self.log_error(error)
            return

        if self._ligado:
            info = f' {self._nome} desligando....'    
            self.log_info(info)
            
        self._ligado = False
        

