import pytest
from datetime import date

from financeiro.pedido import Pedido
from financeiro.cupom import Cupom
from financeiro.estrategias.desconto_percentual import DescontoPercentual
from financeiro.estrategias.frete_fixo import FreteFixo
from financeiro.estrategias.frete_gratis_acima_de import FreteGratisAcimaDe


def test_pedido_sem_cupom_com_frete_fixo():
    pedido = Pedido(200, FreteFixo(15))

    assert pedido.calcular_valor_final() == 215


def test_pedido_com_cupom_e_frete_fixo():
    cupom = Cupom(DescontoPercentual(10), date(2026, 12, 31))
    pedido = Pedido(200, FreteFixo(15), cupom)

    assert pedido.calcular_valor_final(date(2026, 11, 15)) == 195


def test_pedido_com_desconto_e_frete_gratis():
    cupom = Cupom(DescontoPercentual(10), date(2026, 12, 31))
    frete = FreteGratisAcimaDe(180, 15)
    pedido = Pedido(200, frete, cupom)

    assert pedido.calcular_valor_final(date(2026, 11, 15)) == 180


def test_pedido_com_cupom_vencido():
    cupom = Cupom(DescontoPercentual(10), date(2026, 11, 14))
    pedido = Pedido(200, FreteFixo(15), cupom)

    with pytest.raises(ValueError, match="cupom está vencido"):
        pedido.calcular_valor_final(date(2026, 11, 15))


def test_pedido_nao_aceita_total_negativo():
    with pytest.raises(ValueError):
        Pedido(-200, FreteFixo(15))
