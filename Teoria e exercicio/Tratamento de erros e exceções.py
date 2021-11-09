"""
pythonn excptionn list
 - Para tratar exceções usamos o comando:

 - try:
Quais comando que normalmente dariam problemas
 - except:
 se eu tentar coisa de cima é falhar, o que vai acontecer. 
 - else:
 área do que deu certo
- finally:
Vai acontecer independente se deu certo ou erro
===========================================================
Podemos ter varios tipos de except,é cada um deles vai ter seu bloco com sua própria mensagem e o próprio tratamento exemplo:
except TypeError:

except ValueError:

except OSError:


try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que voce digitou')

except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')

except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__class__}')
 else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')

"""
