def leiainteiro(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(print(f'Error!!! - Digite um número inteiro válido'))
            continue
        except (KeyboardInterrupt):
            print('\nUsuário preferiu não digitar esse número!')
            return 0
        else:
            return n 

def leiareal(msg):
    while True:
        try:
            r = float(input(msg))
        except (ValueError, TypeError):
            print('Error!!!- Digite um número real válido')
            continue
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar esse número!')
            return 0
        else:
            return r
