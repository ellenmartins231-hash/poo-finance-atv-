import pytest

from financeiro.estrategias.estrategia_correcao import EstrategiaCorrecao
from financeiro.estrategias.correcao_ipca import CorrecaoIPCA
from financeiro.estrategias.correcao_inpc import CorrecaoINPC


def test_calcular_correcao_ipca():
    estrategia = CorrecaoIPCA(5)

    resultado = estrategia.calcular(1000)

    assert resultado == 1050


def test_calcular_correcao_inpc():
    estrategia = CorrecaoINPC(3)

    resultado = estrategia.calcular(1000)

    assert resultado == 1030


def test_ipca_nao_aceita_taxa_negativa():
    with pytest.raises(ValueError):
        CorrecaoIPCA(-5)


def test_inpc_nao_aceita_taxa_negativa():
    with pytest.raises(ValueError):
        CorrecaoINPC(-3)


def test_ipca_nao_aceita_valor_negativo():
    estrategia = CorrecaoIPCA(5)

    with pytest.raises(ValueError):
        estrategia.calcular(-1000)


def test_inpc_nao_aceita_valor_negativo():
    estrategia = CorrecaoINPC(3)

    with pytest.raises(ValueError):
        estrategia.calcular(-1000)


def test_estrategia_correcao_e_abstrata():
    with pytest.raises(TypeError):
        EstrategiaCorrecao()
