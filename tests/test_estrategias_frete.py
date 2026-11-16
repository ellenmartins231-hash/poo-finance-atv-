import pytest

from financeiro.estrategias.frete_fixo import FreteFixo
from financeiro.estrategias.frete_gratis_acima_de import FreteGratisAcimaDe


def test_frete_fixo():
    estrategia = FreteFixo(15)
    assert estrategia.calcular(200) == 15


def test_frete_fixo_nao_aceita_valor_negativo():
    with pytest.raises(ValueError):
        FreteFixo(-15)


def test_frete_fixo_nao_aceita_total_negativo():
    estrategia = FreteFixo(15)

    with pytest.raises(ValueError):
        estrategia.calcular(-200)


def test_frete_gratis_acima_do_valor_minimo():
    estrategia = FreteGratisAcimaDe(200, 15)
    assert estrategia.calcular(250) == 0


def test_frete_gratis_no_valor_minimo():
    estrategia = FreteGratisAcimaDe(200, 15)
    assert estrategia.calcular(200) == 0


def test_frete_cobrado_abaixo_do_valor_minimo():
    estrategia = FreteGratisAcimaDe(200, 15)
    assert estrategia.calcular(150) == 15


def test_frete_gratis_nao_aceita_valores_negativos():
    with pytest.raises(ValueError):
        FreteGratisAcimaDe(-200, 15)

    with pytest.raises(ValueError):
        FreteGratisAcimaDe(200, -15)
