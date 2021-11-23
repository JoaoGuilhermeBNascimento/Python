# na poo existe varios tipos de relações 
# associação, onde uma classe se relaciona com outra classe, mas nenhuma das duas dependem uma da outra.

from Poo.Associação.classes import *

escritor = escritor ('João')
print(escritor.nome)

Caneta = Caneta('Mont blanc')
print(Caneta.marca)

MaquinaDeEscrever = MaquinaDeEscrever('XL23')
print(MaquinaDeEscrever.label)
print(escritor.nome)
print(Caneta.marca)
Caneta.escrever()


escritor.ferramenta = MaquinaDeEscrever
escritor.ferramenta.escrever('xl')

del escritor

print(Caneta.marca)
MaquinaDeEscrever.escrever('') 