import pytest

from financeiro.estrategias.rendimento_poupanca import RendimentoPoupanca
from financeiro.estrategias.rendimento_cdb import RendimentoCDB
from financeiro.estrategias.estrategia_rendimento import EstrategiaRendimento


def test_rendimento_poupanca():
    estrategia = RendimentoPoupanca(0.5)

    resultado = estrategia.calcular(1000)

    assert resultado == 5


def test_rendimento_cdb():
    estrategia = RendimentoCDB(1.2)

    resultado = estrategia.calcular(1000)

    assert resultado == 12


def test_poupanca_nao_aceita_taxa_negativa():
    with pytest.raises(ValueError):
        RendimentoPoupanca(-0.5)


def test_cdb_nao_aceita_taxa_negativa():
    with pytest.raises(ValueError):
        RendimentoCDB(-1.2)


def test_poupanca_nao_aceita_valor_negativo():
    estrategia = RendimentoPoupanca(0.5)

    with pytest.raises(ValueError):
        estrategia.calcular(-100)


def test_cdb_nao_aceita_valor_negativo():
    estrategia = RendimentoCDB(1.2)

    with pytest.raises(ValueError):
        estrategia.calcular(-100)


def test_estrategia_rendimento_e_uma_interface_abstrata():
    with pytest.raises(TypeError):
        EstrategiaRendimento()