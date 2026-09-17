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
    except ValueError as erro:
        raise ValueError(f'"{texto}" não é um número válido.') from erro

    if math.isnan(valor) or math.isinf(valor):
        raise ValueError('O valor digitado não é um número válido.')

    return valor


# --- Operações ---

def somar(parcela1: float, parcela2: float) -> float:
    """Retorna a soma entre dois números."""
    return parcela1 + parcela2


def subtracao(minuendo: float, subtraendo: float) -> float:
    """Retorna 'minuendo' menos 'subtraendo'."""
    return minuendo - subtraendo


def multiplicacao(fator1: float, fator2: float) -> float:
    """Retorna a multiplicação entre dois números."""
    return fator1 * fator2


def divisao(dividendo: float, divisor: float) -> float:
    """Retorna a divisão entre dois números. Lança ZeroDivisionError se o divisor for zero."""
    if divisor == 0:
        raise ZeroDivisionError('Não é possível dividir por zero.')
    return dividendo / divisor


def potencia(base: float, expoente: float) -> float:
    """Retorna 'base' elevado a 'expoente'.

    Lança ValueError se o resultado não for um número real ou se for
    grande demais para ser representado.
    """
    if base < 0 and expoente != int(expoente):
        raise ValueError('Não é possível elevar um número negativo a um expoente fracionário.')

    try:
        resultado = base ** expoente
    except OverflowError as erro:
        raise ValueError('O resultado é grande demais para ser calculado.') from erro

    if math.isinf(resultado):
        raise ValueError('O resultado é grande demais para ser calculado.')

    return float(resultado)


def raiz_quadrada(numero: float) -> float:
    """Retorna a raiz quadrada de 'número'. Lança ValueError se 'número' for negativo."""
    if numero < 0:
        raise ValueError('Não é possível calcular a raiz quadrada de um número negativo.')
    return math.sqrt(numero)


def porcentagem(percentual: float, valor: float) -> float:
    """Calcula quanto é 'percentual' por cento de 'valor'."""
    return (percentual / 100) * valor

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