"""

Modularização

- Foco: dividir um programa grande
- Foco: Aumentar a legibilidade
- Foco: facilitar a manutenção

from uteis import fatorial,dobro,triplo


num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f' O dobro de {num} é {dobro(num)}')
print(f' O triplo de {num} é {triplo(num)}')
========================================
2 forma
import uteis

num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f' O dobro de {num} é {uteis.dobro(num)}')
print(f' O triplo de {num} é {uteis.triplo(num)}')

from uteis import fatorial,dobro,triplo


num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f' O dobro de {num} é {dobro(num)}')
print(f' O triplo de {num} é {triplo(num)}')

import uteis

num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f' O dobro de {num} é {uteis.dobro(num)}')
print(f' O triplo de {num} é {uteis.triplo(num)}')
        
======================================================================
            VANTAGENS
 - Organização do código
 - facilidade na manutenção
 - ocultação de código detalhado
 - reutilização em outros projetos 
======================================================================
            PACOTES

# Control + shift + L
troca todos os elementos daquele mesmo nome em todos os lugares
"""


from uteis import numeros


num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f' O dobro de {num} é {numeros.dobro(num)}')
print(f' O triplo de {num} é {numeros.triplo(num)}')