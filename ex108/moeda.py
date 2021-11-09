def dobro(n = 0):
    return n*2


def metade(n = 0):
    return n/2


def aumento(n = 0):
    mais = n + (n*0.1)
    return mais


def diminuir(n = 0):
    desconto = n - (n*0.13)
    return desconto


def moeda(n = 0, moeda = 'R$'):
    return f'{moeda} {n:>.2f}'.replace('.',',') # oito casas decimais alinhados a direita


