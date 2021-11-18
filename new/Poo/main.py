from Pessoas import Pessoa

p1 = Pessoa ('Luiz', 24)
p2 = Pessoa ('João', 60)

p1.falar('POO')
p2.comer('sorvete')
p1.comer('churrasco')

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

print(Pessoa.ano_atual)