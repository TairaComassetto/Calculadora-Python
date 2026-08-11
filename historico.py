from copy import deepcopy

class Historico:
    """Armazena e organiza as operações realizadas na calculadora."""

    def __init__(self) -> None:
        self._historico: list[dict] = []
        self._sessao_atual: int = 1

    def adicionar(self, operacao: str, resultado: float | None, n1: float, n2: float) -> None:
        """Adiciona uma operação ao histórico"""
        self._historico.append({
            'operacao': operacao,
            'resultado': resultado,
            'numeros': (n1, n2),
            'sessao': self._sessao_atual
        })

    def obter(self) -> list[dict]:
        """Retorna uma cópia do histórico."""
        return deepcopy(self._historico)

    def limpar(self) -> None:
        """Remove todas as operações do histórico."""
        self._historico.clear()

    def nova_sessao(self) -> None:
        """Inicia uma nova sessão de cálculos."""
        self._sessao_atual += 1