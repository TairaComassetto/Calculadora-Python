"""Testes da lógica matemática (calculo.py)."""

import math

import pytest

from calculo import (
    OPERACOES,
    divisao,
    multiplicacao,
    porcentagem,
    potencia,
    raiz_quadrada,
    somar,
    subtracao,
    validar_numero,
)


class TestValidarNumero:
    """Testes de validar_numero: conversão de texto para número."""

    @pytest.mark.parametrize(
        'texto, esperado',
        [('5', 5.0), ('  7  ', 7.0), ('-3.5', -3.5), ('2e3', 2000.0), ('0', 0.0)],
    )
    def test_converte_textos_validos(self, texto, esperado):
        assert validar_numero(texto) == esperado

    @pytest.mark.parametrize('texto', ['', '   ', 'abc', '5,5', '1 2', 'nan', 'inf'])
    def test_rejeita_textos_invalidos(self, texto):
        with pytest.raises(ValueError):
            validar_numero(texto)

    def test_rejeita_numero_grande_demais(self):
        # 1e400 é maior que o float máximo representável -> vira infinito
        with pytest.raises(ValueError):
            validar_numero('1e400')


class TestOperacoesBasicas:
    """Testes das quatro operações básicas."""

    def test_somar(self):
        assert somar(2, 3) == 5
        assert somar(-1, 1) == 0
        assert somar(2.5, 2.5) == 5.0

    def test_subtracao_respeita_a_ordem(self):
        # subtracao(a, b) -> a - b. No main.py, a pergunta "De qual número
        # você quer subtrair?" alimenta o 'a', e "Quanto?" alimenta o 'b'.
        assert subtracao(10, 3) == 7
        assert subtracao(3, 10) == -7

    def test_multiplicacao(self):
        assert multiplicacao(4, 2.5) == 10
        assert multiplicacao(7, 0) == 0

    def test_divisao(self):
        assert divisao(10, 4) == 2.5

    def test_divisao_por_zero_levanta_erro(self):
        with pytest.raises(ZeroDivisionError):
            divisao(10, 0)


class TestPotencia:
    """Testes de potencia, incluindo os casos que causavam o bug original."""

    def test_calculo_simples(self):
        assert potencia(2, 3) == 8
        assert potencia(9, 0.5) == 3
        assert potencia(5, 0) == 1

    def test_expoente_negativo(self):
        # Expoente negativo é matematicamente válido (1 / base**|expoente|).
        assert potencia(2, -1) == 0.5
        assert potencia(2, -2) == 0.25

    def test_base_negativa_com_expoente_inteiro_funciona(self):
        assert potencia(-2, 3) == -8
        assert potencia(-2, 2) == 4

    def test_base_negativa_com_expoente_fracionario_levanta_erro(self):
        # Antes da correção, isso retornava um número complexo e quebrava
        # o programa ao tentar formatar o resultado.
        with pytest.raises(ValueError):
            potencia(-8, 0.5)

    def test_resultado_grande_demais_levanta_value_error(self):
        # Antes da correção, isso derrubava o programa com OverflowError
        # não tratado.
        with pytest.raises(ValueError):
            potencia(10.0, 1000)


class TestRaizQuadrada:
    """Testes de raiz_quadrada."""

    def test_calculo_simples(self):
        assert raiz_quadrada(16) == 4
        assert raiz_quadrada(0) == 0

    def test_numero_negativo_levanta_erro(self):
        with pytest.raises(ValueError):
            raiz_quadrada(-9)


class TestPorcentagem:
    """Testes de porcentagem."""

    def test_calculo_simples(self):
        assert porcentagem(10, 200) == 20
        assert porcentagem(50, 80) == 40

    def test_zero_por_cento(self):
        assert porcentagem(0, 500) == 0

    def test_percentual_negativo(self):
        # percentual negativo é matematicamente válido (ex: um desconto
        # invertido, ou uma redução expressa como percentual negativo).
        assert porcentagem(-10, 200) == -20

    def test_percentual_acima_de_cem(self):
        # 150% de 200 é um valor maior que o próprio 'valor' -- comportamento
        # esperado, não deveria ser bloqueado.
        assert porcentagem(150, 200) == 300


class TestCatalogoDeOperacoes:
    """Testes do dicionário OPERACOES e da classe Operacao."""

    def test_todas_as_operacoes_executam_sem_erro(self):
        for operacao in OPERACOES.values():
            argumentos = [4.0] * operacao.ariedade
            resultado = operacao.funcao(*argumentos)
            assert isinstance(resultado, float)
            assert math.isfinite(resultado)

    def test_codigos_do_menu_sao_os_esperados(self):
        assert set(OPERACOES) == {'1', '2', '3', '4', '5', '6', '7'}

    def test_ariedade_bate_com_a_operacao(self):
        # Só a raiz quadrada pede um único número; as demais pedem dois.
        assert OPERACOES['6'].ariedade == 1
        for codigo, operacao in OPERACOES.items():
            if codigo != '6':
                assert operacao.ariedade == 2