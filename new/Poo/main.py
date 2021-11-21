from Pessoas import Pessoa

""" p1 = Pessoa ('Luiz', 24)
p2 = Pessoa ('João', 60)

 p1.falar('POO')
p2.comer('sorvete')
p1.comer('churrasco')

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
 """ 
#  p1 = Pessoa.por_ano_nascimento('Luiz',  1987)
p1 = Pessoa('Luiz', 34)
print(p1)
print(p1.nome,p1.idade)
print(p1.get_ano_nascimento())

# Quando for criar o metodo da classe ou da instância, pensar se o metodo é relacionado a classe como um todo ou a instância definida por init