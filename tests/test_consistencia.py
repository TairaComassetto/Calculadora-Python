"""Testes de consistência entre calculo.py e main.py (interface de terminal)."""

from calculo import OPERACOES
from main import PERGUNTAS


class TestConsistenciaOperacoes:
    """A ariedade de cada Operacao deve bater com a quantidade de perguntas."""

    def test_toda_operacao_tem_entrada_em_perguntas(self):
        assert set(OPERACOES) == set(PERGUNTAS)

    def test_quantidade_de_perguntas_bate_com_a_ariedade(self):
        for codigo, operacao in OPERACOES.items():
            assert len(PERGUNTAS[codigo]) == operacao.ariedade, (
                f"Operação '{operacao.nome}' (código {codigo}): "
                f'ariedade={operacao.ariedade}, '
                f'mas PERGUNTAS tem {len(PERGUNTAS[codigo])} pergunta(s).'
            )
