import math

def validar_numero(texto: str) -> float:
    """Converte um texto em número, validando o formato."""
    texto = texto.strip()

    if not texto:
        raise ValueError('Nenhum valor foi digitado.')

    try:
        valor = float(texto)
    except ValueError:
        raise ValueError(f'"{texto}" não é um número válido.')

    if math.isnan(valor) or math.isinf(valor):
        raise ValueError('O valor digitado não é um número válido.')

    return valor

def pedir_numeros():
    """Solicita dois números ao usuário e retorna ambos."""
    n1 = validar_numero(input('Digite um número: '))
    n2 = validar_numero(input('Digite outro número: '))
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
