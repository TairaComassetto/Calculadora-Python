"""Armazenamento do histórico de cálculos, com persistência em JSON."""

import json
from copy import deepcopy
from pathlib import Path

ARQUIVO_HISTORICO = Path(__file__).parent / 'historico.json'


class Historico:
    """Armazena e organiza as operações realizadas na calculadora.

    O histórico é salvo automaticamente em disco a cada alteração
    (adicionar ou limpar), e é carregado do disco ao ser criado.
    """

    def __init__(self, arquivo: Path = ARQUIVO_HISTORICO) -> None:
        self._arquivo: Path = arquivo
        self._historico: list[dict] = self._carregar()

    def _carregar(self) -> list[dict]:
        """Lê o histórico salvo em disco, se existir e for válido.

             Retorna uma lista vazia se o arquivo não existir ou estiver
             corrompido -- um histórico salvo é conveniência, não algo
             essencial ao funcionamento do programa.
             """
        if not self._arquivo.exists():
            return []

        try:
            with open(self._arquivo, encoding='utf-8') as f:
                dados = json.load(f)
        except (json.JSONDecodeError, OSError):
            print('[Aviso] Não foi possível carregar o histórico salvo. Começando do zero.')
            return []

        # numeros é salvo como lista (JSON não tem tupla) e precisa
        # voltar a ser tupla ao carregar.
        return [
            {
                'simbolo': item['simbolo'],
                'numeros': tuple(item['numeros']),
                'resultado': item['resultado'],
            }
            for item in dados
        ]

    def _salvar(self) -> None:
        """Grava o histórico atual em disco."""
        try:
            with open(self._arquivo, 'w', encoding='utf-8') as f:
                json.dump(self._historico, f, ensure_ascii=False, indent=2)
        except OSError:
            print('[Aviso] Não foi possível salvar o histórico em disco.')

    def adicionar(self, simbolo: str, numeros: tuple[float, ...], resultado: float) -> None:
        """Adiciona uma operação ao histórico, guardando os dados brutos (sem formatação)."""
        self._historico.append({
            'simbolo': simbolo,
            'numeros': numeros,
            'resultado': resultado,
        })
        self._salvar()

    def obter(self) -> list[dict]:
        """Retorna uma cópia do histórico."""
        return deepcopy(self._historico)

    def limpar(self) -> None:
        """Remove todas as operações do histórico, em memória e em disco."""
        self._historico.clear()
        self._salvar()
