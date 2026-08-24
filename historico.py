from copy import deepcopy

class Historico:
    """Armazena e organiza as operações realizadas na calculadora."""

    def __init__(self) -> None:
        self._historico: list[dict] = []

    def adicionar(self, operacao: str, resultado: float | None, numeros: tuple[float, ...]) -> None:
        """Adiciona uma operação ao histórico"""
        self._historico.append({
            'operacao': operacao,
            'resultado': resultado,
            'numeros': numeros
        })

    def obter(self) -> list[dict]:
        """Retorna uma cópia do histórico."""
        return deepcopy(self._historico)

    def limpar(self) -> None:
        """Remove todas as operações do histórico."""
        self._historico.clear()
