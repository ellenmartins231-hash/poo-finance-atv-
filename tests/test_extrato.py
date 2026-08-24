from datetime import date

from financeiro.categoria import Categoria
from financeiro.lancamento import Lancamento
from financeiro.fechamento import Fechamento
from financeiro.extrato import Extrato


class TestExtrato:

    def test_cria_extrato_com_fechamentos(self) -> None:
        categoria = Categoria("Eletrônicos")

        lancamento = Lancamento(
            "Compra de teclado",
            250.0,
            date(2026, 8, 10),
            categoria,
        )

        fechamento = Fechamento(
            date(2026, 8, 1),
            date(2026, 8, 31),
            [lancamento],
        )

        extrato = Extrato([fechamento])

        assert extrato.fechamentos == [fechamento]

    def test_calcula_total_dos_fechamentos(self) -> None:
        categoria = Categoria("Eletrônicos")

        lancamento1 = Lancamento(
            "Compra de teclado",
            250.0,
            date(2026, 8, 10),
            categoria,
        )

        lancamento2 = Lancamento(
            "Compra de mouse",
            150.0,
            date(2026, 8, 15),
            categoria,
        )

        fechamento1 = Fechamento(
            date(2026, 8, 1),
            date(2026, 8, 15),
            [lancamento1],
        )

        fechamento2 = Fechamento(
            date(2026, 8, 16),
            date(2026, 8, 31),
            [lancamento2],
        )

        extrato = Extrato([fechamento1, fechamento2])

        assert extrato.total() == 400.0