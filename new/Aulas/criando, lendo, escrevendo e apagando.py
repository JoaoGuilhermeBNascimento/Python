""" 'r' = open for reading(default)

'w' = open for writing, truncating the file first

'x' = open for exclusive creation, failing if the file already exists

'a' de append = open for writing, appending to the end of file if it exists

'b' = binary mode

't' = text mode(default)

'+' = open for updating(reading and writing)
 

file = open('abc.txt','w+')
file.write('linha 1\n')         
file.write('linha 2\n')
file.write('linha 3\n')

file.seek(0, 0) # Relativos a posição do arquivo, 0,0 retorna ao topo do arquivo 

print('Lendo Linhas:')
print(file.read())
print('########')
#imprescindivel fechar o arquivo
file.seek(0,0)
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print('########')

file.seek(0,0)
for linha in file:  # ou file: or file.readlines(): both ways work
    print(linha, end='')
#print(file.readlines())
file.close()
==================================================
2 maneira de fazer
try:
    file = open('abc.txt', 'w+')
    
    file.write('Linha')
    file.seek(0)
    print(file.read())
finally:
    file.close()

# GERENCIADOR DE CONTEXTO
with open('abc.txt','w+') as file:
    file.write('linha1\n')
    file.write('linha2\n')
    file.write('linha3\n')
    
    file.seek(0)
    print(file.read())


with open('abc.txt', 'r') as file:
    
    
    print(file.read())
###############################
with open('abc.txt', 'w+') as file:
    file.write('Outra linha\n')
    file.seek(0)
    print(file.read())
"""
import json

d1 = {
    'Pessoa 1': {
        'nome':'Luiz',
        'idade': 25
    },
    'Pessoa 2' :{
        'Pessoa 2': {
            'nome': 'Rose',
            'idade': 30,
    }

    }
}

d1_json = json.dumps(d1, indent=True)

with open('abc.json','w+') as file:
    file.write(d1_json)

