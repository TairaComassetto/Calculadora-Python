from copy import deepcopy

class Historico:
    """Armazena e organiza as operações realizadas na calculadora."""

    def __init__(self) -> None:
        self._historico: list[dict] = []

    def adicionar(self, simbolo: str, numeros: tuple[float, ...], resultado: float) -> None:
        """Adiciona uma operação ao histórico, guardando os dados brutos (sem formatação)."""
        self._historico.append({
            'simbolo': simbolo,
            'numeros': numeros,
            'resultado': resultado,
        })

    def obter(self) -> list[dict]:
        """Retorna uma cópia do histórico."""
        return deepcopy(self._historico)

    def limpar(self) -> None:
        """Remove todas as operações do histórico."""
        self._historico.clear()
