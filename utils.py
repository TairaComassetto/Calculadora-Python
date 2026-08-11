from time import sleep

def formatar_numero(numero: float | None) -> int | float | None:
    """Remove casas decimais desnecessárias na exibição."""
    if numero is None:
        return None
    return int(numero) if numero == int(numero) else numero

def pausa_curta() -> None:
    sleep(0.8)

def pausa_media() -> None:
    sleep(1)

def pausa_longa() -> None:
    sleep(3)