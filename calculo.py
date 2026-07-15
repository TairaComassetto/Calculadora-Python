def pedir_numeros():
    """Solicita dois números ao usuário e retorna ambos."""
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))
    return n1, n2


def somar(a, b):
    """Retorna a soma entre dois números."""
    return a + b


def subtracao(a, b):
    """Retorna a subtração entre dois números."""
    return a - b


def multiplicacao(a, b):
    """Retorna a multiplicação entre dois números."""
    return a * b


def divisao(a, b):
    """Retorna a divisão entre dois números ou None caso o divisor seja zero."""
    if b == 0:
        return None
    return a / b

Operacoes = {
    '1': (somar, '+', '+'),
    '2': (subtracao, '-', '-'),
    '3': (multiplicacao, '*', 'x'),
    '4': (divisao, '/', '/'),
}
