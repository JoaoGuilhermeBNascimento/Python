"""
CORES NO TERMINAL
  ANSI = escape sequence
  sempre que quiser representar uma cor começar com \033  aqui [m - no aqui primeiro a gente representa o style;depois o text; e então o back(cor de fundo)
códigos para estilo
0 - nada
1 = em negrito - bold
4 = Underline = sublinhado
7 - Inverter as configurações - negative 

as opções de cores é do 30 a 37 
30 - branca 31 - vermelha - 32 verde - 33 - amarela 34 - azul 35 - roxo - 36 azul bb - 37 - cinza  ( CORES DE TEXTO)
40 '' '' 41 42 43 44 45 46 47 - mesmas  corse do text mas agora no background 
para letra preta e fundo branco usamos \33[7:30m
  \033[0;33;44m
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a, b))
print ( ' Olá Muito prazer em te conhecer, {}{}'.format('\033[4;34m',nome, '\033[m'))

metodo 3
cores = {'limpa':'\033[m',
'azul':'\033[34m',
'amarelo':'\033[33m',
'pretoebranco':'\33[7;30'}
print ( ' Olá Muito prazer em te conhecer, {}{}'.format(cores['pretoebranco'], nome, cores ['limpa']))
"""
n = 'josé'
i = 25