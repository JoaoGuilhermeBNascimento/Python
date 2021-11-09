from types import resolve_bases


def dobro(n = 0,formato = False):
    res = n*2
    return res if formato == False else moeda(res)


def metade(n = 0, formato = False):
    res = n/2
    return res if formato is False else moeda(res)


def aumento(n = 0, formato = False):
    mais = n + (n*0.1)
    return mais if not format else moeda(mais)


def diminuir(n = 0, formato = False):
    desconto = n - (n*0.13)
    return desconto if formato is False else moeda(desconto)


def moeda(n = 0, moeda = 'R$'):
    return f'{moeda} {n:>.2f}'.replace('.',',') # oito casas decimais alinhados a direita


