""" 
class A:
    vc = 123

a1 = A()
a2 = A()

# Quando fazemos dessa forma estou criando um atributo direto na minha instância como no caso abaixo:
a1.vc = 321
a2.cv = 987

print(a1.__dict__)
print(a2.__dict__)
print(A.__dict__)

print(a1.vc)
print(a2.vc)
print(A.vc) 

 """

class A:
    vc = 123

    def __init__(self):
        self.vc = 321

a1 = A()
a2 = A()
A.vc = 'Alterado'

print(a1.vc)
print(a2.vc)
print(A.vc)
        