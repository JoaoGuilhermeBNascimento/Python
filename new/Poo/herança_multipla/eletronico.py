class Eletronico:
    def __init__(self, nome,) -> None:
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if  self._ligado:
            print(f' {self._nome} está ligando!')
            return
        print(f' {self._nome} ligado!!')
        self._ligado = True

    def desligar(self):
        if not self._ligado:
            print(f'{self._nome}, não da para desligar, pois já está desligado')
            return

        print(f' {self._nome} desligando...')
        self._ligado = False

