class Pessoa:# super classe
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f' {self.nomeclasse} Falando')
# estou deixando claro que Cliente e Aluno, herdam de pessoa
class Cliente(Pessoa): # subclasse
    def comprar(self):
        print(f' {self.nomeclasse} comprando....')

    def falar(self):
        print('estou em cliente')


class Aluno(Pessoa):  # subclasse
    def estudar(self):
        print(f' {self.nomeclasse} estudando...')

#### sobreposição de membros a partir daqui.
# está classe de clienteVIP tem tudo que tem na classe Pessoa e na classe Cliente.


class ClienteVip(Cliente):  # é um cliente e uma pessoa, pois está na cadeia de Pessoa # subclasse
    def __init__(self, nome, idade, sobrenome) -> None:
        super().__init__(nome, idade) # poderia chamar a classe pessoa, colocando o self como primeiro argumento ↓↓↓
        #Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f' {self.nome} {self.sobrenome} idade: {self.idade}')


    """ def falar(self): # sobrepos a def falar que estava em Pessoa
        Pessoa.falar(self)
        Cliente.falar(self)
        #super().falar() # está se referindo a super classe(Pessoa) PODE USAR SUPER OU CHAMAR A CLASSE DIRETO INSTÂNCIANDO
        print('outra coisa qlq')
 """