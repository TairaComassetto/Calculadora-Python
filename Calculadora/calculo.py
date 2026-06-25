def pedir_numeros():
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))
    return n1, n2


def somar(a,b):
    return a + b


def subtracao(a,b):
    return a - b


def multiplicacao(a,b):
    return a * b


def divisao(a,b):
    if b == 0:
        return None
    return a /b