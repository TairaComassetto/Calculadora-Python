from time import sleep

def formatar_numero(numero):
    """Remove casas decimais desnecessárias na exibição."""
    if numero is None:
        return None
    return int(numero) if numero == int(numero) else numero

def pausa_curta():
    sleep(0.8)

def pausa_media():
    sleep(1)

def pausa_longa():
    sleep(3)