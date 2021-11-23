"""
métodos e atributos usados para proteger sua aplicação.
public, protected, private  

_ protected/private, mas de maneira mais sutil (public_)
__ privado (_nomeclasse__nomeatributo)
recomenda fortemente que esse essa variavel não seja acessado.

"""


class DataBase:
    def __init__(self):
        self.__dados = {} # o atributo __dados é o coração dessa classe3

    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]



db = DataBase()
db.inserir_cliente(1, 'Otavio')
db.inserir_cliente(2, 'Miranda')
db.inserir_cliente(3, 'rose')
db.apaga_cliente(2)
print(db.dados)

""" 
db.__dados = ' uma outra coisa'
print(db.__dados)
print(db._DataBase__dados)
db.lista_clientes() """

