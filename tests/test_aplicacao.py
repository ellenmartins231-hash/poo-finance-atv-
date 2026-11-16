import pytest

from financeiro.aplicacao import Aplicacao
from financeiro.estrategias.rendimento_poupanca import RendimentoPoupanca
from financeiro.estrategias.rendimento_cdb import RendimentoCDB


def test_aplicacao_com_rendimento_poupanca():
    aplicacao = Aplicacao(1000, RendimentoPoupanca(0.5))

    assert aplicacao.calcular_rendimento() == 5


def test_aplicacao_com_rendimento_cdb():
    aplicacao = Aplicacao(1000, RendimentoCDB(1.2))

    assert aplicacao.calcular_rendimento() == 12


def test_aplicacao_nao_aceita_valor_negativo():
    with pytest.raises(ValueError):
        Aplicacao(-1000, RendimentoPoupanca(0.5))