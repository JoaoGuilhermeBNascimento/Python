def dobro(n = 0,formato = False):
    res = n*2
    return res if formato == False else moeda(res)


def metade(n = 0, formato = False):
    res = n/2
    return res if formato is False else moeda(res)


def aumento(n = 0, taxa=0, formato = False):
    mais = n + (n*taxa/100)
    return mais if not format else moeda(mais)


def diminuir(n = 0,taxa=0, formato = False):
    desconto = n - (n * taxa/100)
    return desconto if formato is False else moeda(desconto)


def moeda(n = 0, moeda = 'R$'):
    return f'{moeda} {n:>.2f}'.replace('.',',') # oito casas decimais alinhados a direita


def resumo(n=0,taxa= 10,taxar=5):
    print('='*30)
    print('RESUMO DO VALOR'.center(30))
    print('='*30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'A metade do preço: \t{metade(n, True)}')
    print(f'Com {taxa}% de aumento: \t{aumento(n, taxa, True)} ')
    print(f'Com {taxar}% de desconto: \t{diminuir(n,taxar, True)}')
    print('='*30)

