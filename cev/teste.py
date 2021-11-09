
import moeda
import dados

while True:
    n = dados.leiaDinheiro('Digite o preço: R$ ')
    moeda.resumo(n, 20, 12)
    while True:
        resp = str(input('Quer continuar ? [S/N] ')).upper().strip()[0]
        if resp  in 'SN':
            break
        print('Error!! Digite apenas S ou N ')
    if resp == 'N':
        break
print('Volte Sempre.')
