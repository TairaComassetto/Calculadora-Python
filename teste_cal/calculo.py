

def pedir_numeros():
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    return n1, n2


def somar(a,b):
    return a+b


def subtracao(a,b):
    return a-b


def multiplicacao(a,b):
    return a*b


def divisao(a,b):
    if b == 0:
        return 'Não é possivel dividir por zero!'
    return a/b

def novos_numeros():
    print('Digite os novos números.')
    n1 = float(input('Digite o primeiro novo número: '))
    n2 = float(input('Digite o segundo novo número: '))
    return n1, n2