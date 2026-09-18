"""Testes das funções de formatação (utils.py)."""

import pytest

from utils import formatar_numero, formatar_operacao


class TestFormatarNumero:
    """Testes de formatar_numero: arredondamento e remoção de decimais."""

    @pytest.mark.parametrize(
        'entrada, esperado',
        [
            (5.0, 5),
            (5, 5),
            (2.5, 2.5),
            (-3.0, -3),
            (0.0, 0),
            (-2.5, -2.5),
        ],
    )
    def test_remove_decimais_desnecessarios(self, entrada, esperado):
        resultado = formatar_numero(entrada)
        assert resultado == esperado
        # Também confere o tipo: número "inteiro" deve virar int de verdade,
        # não só um float que é numericamente igual a um int.
        if esperado == int(esperado):
            assert isinstance(resultado, int)

    def test_corrige_artefato_de_ponto_flutuante(self):
        # 0.1 + 0.2 em Python puro dá 0.30000000000000004
        assert formatar_numero(0.1 + 0.2) == 0.3

    def test_mantem_casas_decimais_significativas(self):
        assert formatar_numero(3.14159) == 3.14159

    def test_arredonda_alem_da_precisao_configurada(self):
        # CASAS_DECIMAIS = 10, então algo com mais de 10 casas é arredondado.
        assert formatar_numero(1 / 3) == round(1 / 3, 10)


class TestFormatarOperacao:
    """Testes de formatar_operacao: montagem da representação legível."""

    def test_operacao_com_dois_numeros(self):
        assert formatar_operacao('+', (10.0, 5.0)) == '10 + 5'

    def test_operacao_com_um_numero(self):
        assert formatar_operacao('√', (9.0,)) == '√(9)'

    def test_usa_numeros_ja_formatados(self):
        # 10.0 e 4.0 devem aparecer sem o '.0', já que formatar_numero
        # é aplicado a cada valor antes de montar a string.
        assert formatar_operacao('/', (10.0, 4.0)) == '10 / 4'

    def test_numero_negativo(self):
        assert formatar_operacao('+', (-5.0, 3.0)) == '-5 + 3'

    def test_simbolo_de_porcentagem(self):
        assert formatar_operacao('% de', (10.0, 200.0)) == '10 % de 200'