from time import sleep

def formatar_numero(numero: float) -> int | float:
    """Remove casas decimais desnecessárias na exibição."""
    return int(numero) if numero == int(numero) else numero

def formatar_operacao(simbolo: str, numeros: tuple[float, ...]) -> str:
    """Monta a representação legível de uma operação (ex: '10 + 5' ou 'sqrt(9)')."""
    numeros_fmt = [formatar_numero(n) for n in numeros]

    if len(numeros_fmt) == 1:
        return f'{simbolo}({numeros_fmt[0]})'
    return f' {simbolo} '.join(str(n) for n in numeros_fmt)

def pausa_curta() -> None:
    sleep(0.8)

def pausa_media() -> None:
    sleep(1)

def pausa_longa() -> None:
    sleep(3)