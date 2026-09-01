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

def pedir_numeros(perguntas: list[str]) -> tuple[float, ...]:
    """Faz uma pergunta especifica para cada número necessário e retorna todos."""
    numeros = []
    for pergunta in perguntas:
        numeros.append((validar_numero(input(f'{pergunta}: '))))
    return tuple(numeros)


# --- Operações ---

def somar(a: float, b: float) -> float:
    """Retorna a soma entre dois números."""
    return a + b


def subtracao(a: float, b: float) -> float:
    """Retorna a subtração entre dois números."""
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
    """Retorna 'a' elevado a 'b'."""
    return a ** b


def raiz_quadrada(a: float) -> float:
    """Retorna a raiz quadrada de 'a'. Lança ValueError se 'a' for negativo."""
    if a < 0:
        raise ValueError('Não é possível calcular a raiz de um número negativo.')
    return math.sqrt(a)

def porcentagem(a: float, b: float) -> float:
    """Calcula quanto é 'a' por cento de 'b'."""
    return (a / 100) * b


# Cada entrada: (função, perguntas (uma por número necessário), símbolo_interno, símbolo_exibição)
OPERACOES = {
    '1': (somar,          ['Qual é o primeiro número?', 'E o segundo?'],                  '+',    '+'),
    '2': (subtracao,      ['Qual número você quer subtrair?', 'E de qual número?'],        '-',    '-'),
    '3': (multiplicacao,  ['Qual é o primeiro número?', 'E o segundo?'],                  '*',    'x'),
    '4': (divisao,        ['Qual número você quer dividir?', 'E por qual número?'],        '/',    '/'),
    '5': (potencia,       ['Qual é a base?', 'E o expoente?'],                            '**',   '^'),
    '6': (raiz_quadrada,  ['De qual número você quer a raiz quadrada?'],                  'sqrt', '√'),
    '7': (porcentagem,    ['Quantos por cento você quer calcular?', 'De qual valor?'],     '%',    '% de'),
}
