"""Funções auxiliares de formatação e ritmo da interface."""

from time import sleep

CASAS_DECIMAIS = 10


def formatar_numero(numero: float) -> int | float:
    """Arredonda o número e remove casas decimais desnecessárias na exibição.

    O arredondamento evita artefatos de ponto flutuante como
    0.30000000000000004 aparecerem para o usuário.
    """
    arredondado  = round(numero, CASAS_DECIMAIS)
    return int(arredondado) if arredondado == int(arredondado) else arredondado

def formatar_operacao(simbolo: str, numeros: tuple[float, ...]) -> str:
    """Monta a representação legível de uma operação (ex: '10 + 5' ou '√(9)')."""
    numeros_fmt = [formatar_numero(n) for n in numeros]

    if len(numeros_fmt) == 1:
        return f'{simbolo}({numeros_fmt[0]})'
    return f' {simbolo} '.join(str(n) for n in numeros_fmt)


def pausa(segundos: float = 0.25) -> None:
    """Pequena pausa para dar ritmo à interface, sem travar o uso."""
    sleep(segundos)