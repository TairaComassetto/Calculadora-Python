import math
from collections.abc import Callable
from dataclasses import dataclass

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

# --- Operações ---

def somar(a: float, b: float) -> float:
    """Retorna a soma entre dois números."""
    return a + b


def subtracao(a: float, b: float) -> float:
    """Retorna 'a' menos 'b'."""
    return a - b


def multiplicacao(a: float, b: float) -> float:
    """Retorna a multiplicação entre dois números."""
    return a * b


def divisao(a: float, b: float) -> float:
    """Retorna a divisão entre dois números. Lança ZeroDivisionError se o divisor for zero."""
    if b == 0:
        raise ZeroDivisionError('Não é possível dividir por zero.')
    return a / b

def potencia(a: float, b: float) -> float:
    """Retorna 'a' elevado a 'b'.

    Lança ValueError se o resultado não for um número real ou se for
    grande demais para ser representado.
    """
    if a < 0 and b != int(b):
        raise ValueError('Não é possível elevar um número negativo a um expoente fracionário.')

    try:
        resultado = a ** b
    except OverflowError as erro:
        raise ValueError('O resultado é grande demais para ser calculado.') from erro

    if math.isinf(resultado):
        raise ValueError('O resultado é grande demais para ser calculado.')

    return float(resultado)


def raiz_quadrada(a: float) -> float:
    """Retorna a raiz quadrada de 'a'. Lança ValueError se 'a' for negativo."""
    if a < 0:
        raise ValueError('Não é possível calcular a raiz de um número negativo.')
    return math.sqrt(a)

def porcentagem(a: float, b: float) -> float:
    """Calcula quanto é 'a' por cento de 'b'."""
    return (a / 100) * b

# --- Catálogo de operações ---

@dataclass(frozen=True)
class Operacao:
    """Descreve uma operação disponível na calculadora."""

    nome: str
    funcao: Callable[..., float]
    simbolo: str
    ariedade: int

OPERACOES: dict[str, Operacao] = {
    '1': Operacao('Somar', somar, '+', 2),
    '2': Operacao('Subtrair', subtracao, '-', 2),
    '3': Operacao('Multiplicar', multiplicacao, 'x', 2),
    '4': Operacao('Dividir', divisao, '/', 2),
    '5': Operacao('Potência', potencia, '^', 2),
    '6': Operacao('Raiz Quadrada', raiz_quadrada, '√', 1),
    '7': Operacao('Porcentagem', porcentagem, '% de', 2),
}