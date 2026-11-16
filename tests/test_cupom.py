import pytest
from datetime import date

from financeiro.cupom import Cupom
from financeiro.estrategias.desconto_percentual import DescontoPercentual


def test_cupom_aplica_desconto():
    cupom = Cupom(DescontoPercentual(10), date(2026, 12, 31))

    assert cupom.calcular_desconto(200, date(2026, 11, 15)) == 20


def test_cupom_valido_no_dia_do_vencimento():
    cupom = Cupom(DescontoPercentual(10), date(2026, 11, 15))

    assert cupom.calcular_desconto(200, date(2026, 11, 15)) == 20


def test_cupom_vencido_nao_aplica_desconto():
    cupom = Cupom(DescontoPercentual(10), date(2026, 11, 14))

    with pytest.raises(ValueError, match="cupom está vencido"):
        cupom.calcular_desconto(200, date(2026, 11, 15))
