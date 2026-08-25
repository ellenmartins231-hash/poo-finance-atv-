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
            Lancamento.DEBITO,
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
            Lancamento.DEBITO,
        )

        lancamento2 = Lancamento(
            "Compra de mouse",
            150.0,
            date(2026, 8, 15),
            categoria,
            Lancamento.DEBITO,
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

    def test_calcula_total_de_creditos(self) -> None:
        categoria = Categoria("Renda")

        salario = Lancamento(
            "Salário",
            3000.0,
            date(2026, 8, 5),
            categoria,
            Lancamento.CREDITO,
        )

        freelance = Lancamento(
            "Freelance",
            500.0,
            date(2026, 8, 10),
            categoria,
            Lancamento.CREDITO,
        )

        fechamento = Fechamento(
            date(2026, 8, 1),
            date(2026, 8, 31),
            [salario, freelance],
        )

        extrato = Extrato([fechamento])

        assert extrato.total_creditos() == 3500.0

    def test_calcula_total_de_debitos(self) -> None:
        categoria = Categoria("Eletrônicos")

        teclado = Lancamento(
            "Compra de teclado",
            250.0,
            date(2026, 8, 10),
            categoria,
            Lancamento.DEBITO,
        )

        mouse = Lancamento(
            "Compra de mouse",
            150.0,
            date(2026, 8, 15),
            categoria,
            Lancamento.DEBITO,
        )

        fechamento = Fechamento(
            date(2026, 8, 1),
            date(2026, 8, 31),
            [teclado, mouse],
        )

        extrato = Extrato([fechamento])

        assert extrato.total_debitos() == 400.0

    def test_calcula_saldo(self) -> None:
        categoria = Categoria("Financeiro")

        salario = Lancamento(
            "Salário",
            3000.0,
            date(2026, 8, 5),
            categoria,
            Lancamento.CREDITO,
        )

        teclado = Lancamento(
            "Compra de teclado",
            250.0,
            date(2026, 8, 10),
            categoria,
            Lancamento.DEBITO,
        )

        mouse = Lancamento(
            "Compra de mouse",
            150.0,
            date(2026, 8, 15),
            categoria,
            Lancamento.DEBITO,
        )

        fechamento = Fechamento(
            date(2026, 8, 1),
            date(2026, 8, 31),
            [salario, teclado, mouse],
        )

        extrato = Extrato([fechamento])

        assert extrato.saldo() == 2600.0

    def test_extrato_sem_fechamentos(self) -> None:
        extrato = Extrato([])

        assert extrato.total() == 0.0
        assert extrato.total_creditos() == 0.0
        assert extrato.total_debitos() == 0.0
        assert extrato.saldo() == 0.0