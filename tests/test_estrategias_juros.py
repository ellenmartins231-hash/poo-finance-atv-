import pytest

from financeiro.estrategias.estrategia_juros import EstrategiaJuros
from financeiro.estrategias.juros_simples import JurosSimples
from financeiro.estrategias.juros_compostos import JurosCompostos


def test_calcular_juros_simples():
    estrategia = JurosSimples(10)
    assert estrategia.calcular(1000, 2) == 200


def test_calcular_juros_compostos():
    estrategia = JurosCompostos(10)
    assert estrategia.calcular(1000, 2) == pytest.approx(210)


def test_juros_simples_nao_aceita_taxa_negativa():
    with pytest.raises(ValueError):
        JurosSimples(-10)


def test_juros_compostos_nao_aceita_taxa_negativa():
    with pytest.raises(ValueError):
        JurosCompostos(-10)


def test_juros_simples_nao_aceita_valor_negativo():
    with pytest.raises(ValueError):
        JurosSimples(10).calcular(-1000, 2)


def test_juros_compostos_nao_aceita_valor_negativo():
    with pytest.raises(ValueError):
        JurosCompostos(10).calcular(-1000, 2)


def test_juros_simples_nao_aceita_periodos_negativos():
    with pytest.raises(ValueError):
        JurosSimples(10).calcular(1000, -2)


def test_juros_compostos_nao_aceita_periodos_negativos():
    with pytest.raises(ValueError):
        JurosCompostos(10).calcular(1000, -2)


def test_estrategia_juros_e_abstrata():
    with pytest.raises(TypeError):
        EstrategiaJuros()
