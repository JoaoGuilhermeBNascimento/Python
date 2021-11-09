def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'ERROR \"{entrada}\" Preço inválido!!!')
        else:
            valido = True
            return float(entrada)


def leiaint(msg):
    ok = False
    valor = 0 
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Error! Digite um número inteiro válido')
        if ok:
            break
    return valor