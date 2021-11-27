""" class Arquivo:
    def __init__(self, arquivo, modo) -> None:
        print('Abrindo arquivo')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('retornando arquivo')
        # dentro dessa função eu tenho que retornar o que vai vim para dentro da variável arquivo(variavel not the class)
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Fechando arquivo')
        self.arquivo.close()
        # Tratei a exceção
        return True

# Nesse caso, fazemos a class Arquivo se comportar como um gerenciador de contexto.
with Arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('alguma coisa')

# Qualquer coisa que é necessário abrir e depois fechar, podemos utilizar esse context manager, segue exemplos: ↓
# Conexão com base de dados, conexão de rede, arquivo etc.
"""
# melhor método
from contextlib import contextmanager

@contextmanager  # para fazer a função se transformar eu preciso decorar ela com contextmanager
def abrir(arquivo, modo): 
    try:
        print('Abrindo arquivo')
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        print('Fechando arquivo')
        arquivo.close

with abrir('abc.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3')