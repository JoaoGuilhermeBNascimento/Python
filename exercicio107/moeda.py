def dobro(n):
    return n*2


def metade(n):
    return n/2


def aumento(n):
    mais = n + (n*0.1)
    return mais


def diminuir(n):
    desconto = n - (n*0.13)
    return desconto




while True:
    n = dados.leiaDinheiro(input('Digite o preço: R$ '))
    moeda.resumo(n, 20, 12)
    while True:
        resp = str(input('Quer continuar ? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Error! Digite apenas S ou N...')
    if resp in 'N':
        break
print('Volte sempre')

