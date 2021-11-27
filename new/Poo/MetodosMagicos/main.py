"""
 https://rszalski.github.io/magicmethods/ 
 __init__ = costumamos chamar ele de construtor um dos metodos mágicos
 class A:
    def __new__(cls, *args, **kwargs):
        
        #cls.nome = 'Joao Guilherme'
        def haha(*args, **kwargs):
            print('Fala Oi')

        cls.haha = haha


        return object.__new__(cls)
    
    
    def __init__(self) -> None:

        def __call__(self, *args, **kwds) :
        # print(args)
        # print(kwds)
        resultado = 1
a.fala_oi()
print(variavel)
# a(1,2,3,4,5, nome = 'João')

        for i in args:
            resultado *= i
        return resultado

        def __setattr__(self, key, value) -> None:
        if key == 'nome':
            self.__dict__[key] = 'Você não pode fazer isso'
        else:
            self.__dict__[key] = value
            
    
    
"""

class A:
    def __init__(self) -> None:
        pass


    def __len__(self, nome):
        self.nome = nome
        return len(nome)
        

a = A() # uma classe e a instância da classe A


nome = 'João Guilherme'
print(len(nome))
