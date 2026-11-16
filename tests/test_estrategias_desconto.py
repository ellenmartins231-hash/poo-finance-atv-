import pytest

from financeiro.estrategias.desconto_percentual import DescontoPercentual
from financeiro.estrategias.sem_desconto import SemDesconto


def test_desconto_percentual():
    estrategia = DescontoPercentual(10)
    assert estrategia.calcular(200) == 20


def test_desconto_percentual_de_100():
    estrategia = DescontoPercentual(100)
    assert estrategia.calcular(200) == 200


def test_desconto_percentual_nao_aceita_taxa_negativa():
    with pytest.raises(ValueError):
        DescontoPercentual(-10)


def test_desconto_percentual_nao_aceita_taxa_acima_de_100():
    with pytest.raises(ValueError):
        DescontoPercentual(110)


def test_desconto_percentual_nao_aceita_total_negativo():
    estrategia = DescontoPercentual(10)

    with pytest.raises(ValueError):
        estrategia.calcular(-200)


def test_sem_desconto():
    estrategia = SemDesconto()
    assert estrategia.calcular(200) == 0


def test_sem_desconto_nao_aceita_total_negativo():
    estrategia = SemDesconto()

    with pytest.raises(ValueError):
        estrategia.calcular(-200)
