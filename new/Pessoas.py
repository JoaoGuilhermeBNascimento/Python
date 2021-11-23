""" # caso seja nome composto BasePessoa
class Pessoa:
    def falar(self):
        print('Pessoa está falando....')
 """
 # todo e qualquer parametro que eu criar deve ser passado o parametrto self primeiro por convenção
# começa a contar a partir do nome, o self é enviado automaticamente pelo python
# Vale ressaltar que o ano atual no caso é um atributo da classe
# já os def são atributos relacionados com a instância, que no caso é self.
from datetime import datetime
from random import randint

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self,nome,idade,comendo=False,falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return
        
        if self.falando:
            print(f'{self.nome} já está falando sobre')
        
        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return
        
        print(f'{self.nome} parou de falar')
        self.falando = False

    def comer(self,alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return
        if self.falando:
            print(f'{self.nome} não pode comer falando!')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True
        
    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        
        print(f'{self.nome} parou de comer')
        self.comendo = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
   
    @classmethod#decorador
    #não quero me referir a estância eu quero me referir a classe, podendo ser qlq nome que eu quiser, menos class pois é a class criada,normalmente é chamada de cls
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    
    @staticmethod
    # nesse método não utilizamos nem a classe nem a estância, mas deve está dentro da classe por organização
    def gera_id():
        rand = randint(10000, 19999)
        return rand
    
