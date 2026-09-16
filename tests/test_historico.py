"""Testes do histórico de cálculos (historico.py)."""

from historico import Historico


class TestHistorico:
    """Testes da classe Historico."""

    def test_comeca_vazio(self):
        assert Historico().obter() == []

    def test_adiciona_registro(self):
        historico = Historico()
        historico.adicionar('+', (2, 3), 5)

        registros = historico.obter()
        assert len(registros) == 1
        assert registros[0]['simbolo'] == '+'
        assert registros[0]['numeros'] == (2, 3)
        assert registros[0]['resultado'] == 5

    def test_mantem_a_ordem_de_insercao(self):
        historico = Historico()
        historico.adicionar('+', (1, 1), 2)
        historico.adicionar('x', (2, 2), 4)

        simbolos = [item['simbolo'] for item in historico.obter()]
        assert simbolos == ['+', 'x']

    def test_limpar_remove_tudo(self):
        historico = Historico()
        historico.adicionar('+', (1, 1), 2)
        historico.limpar()

        assert historico.obter() == []

    def test_obter_devolve_copia_independente(self):
        # obter() usa deepcopy, então alterar o resultado não pode afetar
        # o histórico interno.
        historico = Historico()
        historico.adicionar('+', (1, 1), 2)

        copia = historico.obter()
        copia.clear()
        copia.append({'simbolo': 'x', 'numeros': (9, 9), 'resultado': 81})

        assert len(historico.obter()) == 1
        assert historico.obter()[0]['simbolo'] == '+'