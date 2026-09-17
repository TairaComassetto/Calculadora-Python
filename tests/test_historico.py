"""Testes do histórico de cálculos (historico.py), incluindo persistência em JSON."""

import json

from historico import Historico


class TestHistorico:
    """Testes da classe Historico, usando um arquivo temporário isolado."""

    def test_comeca_vazio(self, tmp_path):
        arquivo = tmp_path / 'historico.json'
        assert Historico(arquivo).obter() == []

    def test_adiciona_registro(self, tmp_path):
        arquivo = tmp_path / 'historico.json'
        historico = Historico(arquivo)
        historico.adicionar('+', (2, 3), 5)

        registros = historico.obter()
        assert len(registros) == 1
        assert registros[0]['simbolo'] == '+'
        assert registros[0]['numeros'] == (2, 3)
        assert registros[0]['resultado'] == 5

    def test_mantem_a_ordem_de_insercao(self, tmp_path):
        arquivo = tmp_path / 'historico.json'
        historico = Historico(arquivo)
        historico.adicionar('+', (1, 1), 2)
        historico.adicionar('x', (2, 2), 4)

        simbolos = [item['simbolo'] for item in historico.obter()]
        assert simbolos == ['+', 'x']

    def test_limpar_remove_tudo(self, tmp_path):
        arquivo = tmp_path / 'historico.json'
        historico = Historico(arquivo)
        historico.adicionar('+', (1, 1), 2)
        historico.limpar()

        assert historico.obter() == []

    def test_obter_devolve_copia_independente(self, tmp_path):
        # obter() usa deepcopy, então alterar o resultado não pode afetar
        # o histórico interno.
        arquivo = tmp_path / 'historico.json'
        historico = Historico(arquivo)
        historico.adicionar('+', (1, 1), 2)

        copia = historico.obter()
        copia.clear()
        copia.append({'simbolo': 'x', 'numeros': (9, 9), 'resultado': 81})

        assert len(historico.obter()) == 1
        assert historico.obter()[0]['simbolo'] == '+'


class TestPersistenciaEmJson:
    """Testes específicos da persistência em disco."""

    def test_adicionar_salva_no_arquivo(self, tmp_path):
        arquivo = tmp_path / 'historico.json'
        historico = Historico(arquivo)
        historico.adicionar('+', (2, 3), 5)

        assert arquivo.exists()
        with open(arquivo, encoding='utf-8') as f:
            dados = json.load(f)
        assert dados == [{'simbolo': '+', 'numeros': [2, 3], 'resultado': 5}]

    def test_nova_instancia_carrega_do_arquivo(self, tmp_path):
        arquivo = tmp_path / 'historico.json'
        Historico(arquivo).adicionar('^', (2, 3), 8)

        historico_recarregado = Historico(arquivo)
        registros = historico_recarregado.obter()
        assert len(registros) == 1
        assert registros[0]['simbolo'] == '^'
        assert registros[0]['numeros'] == (2, 3)

    def test_numeros_volta_como_tupla_apos_carregar(self, tmp_path):
        arquivo = tmp_path / 'historico.json'
        Historico(arquivo).adicionar('+', (1, 2), 3)

        registros = Historico(arquivo).obter()
        assert isinstance(registros[0]['numeros'], tuple)

    def test_limpar_apaga_conteudo_do_arquivo(self, tmp_path):
        arquivo = tmp_path / 'historico.json'
        historico = Historico(arquivo)
        historico.adicionar('+', (1, 1), 2)
        historico.limpar()

        with open(arquivo, encoding='utf-8') as f:
            dados = json.load(f)
        assert dados == []

    def test_arquivo_inexistente_comeca_vazio_sem_erro(self, tmp_path):
        arquivo = tmp_path / 'nao_existe.json'
        assert Historico(arquivo).obter() == []

    def test_arquivo_corrompido_comeca_vazio_sem_quebrar(self, tmp_path, capsys):
        arquivo = tmp_path / 'historico.json'
        arquivo.write_text('{isso não é json válido', encoding='utf-8')

        historico = Historico(arquivo)
        assert historico.obter() == []

        # Confere que um aviso foi exibido, sem travar o programa.
        saida = capsys.readouterr().out
        assert 'histórico' in saida.lower()
