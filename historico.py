from copy import deepcopy

class Historico:
    """Armazena e organiza as operações realizadas na calculadora."""

    def __init__(self):
        self._historico = []
        self._sessao_atual = 1

    def adicionar(self, operacao: str, resultado, n1, n2):
        """Adiciona uma operação ao histórico"""
        self._historico.append({
            'operacao': operacao,
            'resultado': resultado,
            'numeros': (n1, n2),
            'sessao': self._sessao_atual
        })

    def obter(self):
        """Retorna uma cópia do histórico."""
        return deepcopy(self._historico)

    def limpar(self):
        """Remove todas as operações do histórico."""
        self._historico.clear()

    def sessao_nova(self):
        """Inicia uma nova sessão de cálculos."""
        self._sessao_atual += 1