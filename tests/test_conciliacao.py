from datetime import date
from financeiro.categoria import Categoria
from financeiro.lancamento import Lancamento
from financeiro.fechamento import Fechamento
from financeiro.conciliacao import Conciliacao


class TestConciliacao:

    def test_debitos_e_creditos_iguais_estao_conciliados(self) -> None:
        categoria = Categoria("Financeiro")

        credito = Lancamento(
            "Salário",
            1000.0,
            date(2026, 8, 10),
            categoria,
            Lancamento.CREDITO,
        )

        debito = Lancamento(
            "Compra",
            1000.0,
            date(2026, 8, 15),
            categoria,
            Lancamento.DEBITO,
        )

        fechamento = Fechamento(
            date(2026, 8, 1),
            date(2026, 8, 31),
            [credito, debito],
        )

        conciliacao = Conciliacao(fechamento)

        assert conciliacao.esta_conciliado() is True

    def test_debitos_e_creditos_diferentes_nao_estao_conciliados(self) -> None:
        categoria = Categoria("Financeiro")

        credito = Lancamento(
            "Salário",
            1000.0,
            date(2026, 8, 10),
            categoria,
            Lancamento.CREDITO,
        )

        debito = Lancamento(
            "Compra",
            900.0,
            date(2026, 8, 15),
            categoria,
            Lancamento.DEBITO,
        )

        fechamento = Fechamento(
            date(2026, 8, 1),
            date(2026, 8, 31),
            [credito, debito],
        )

        conciliacao = Conciliacao(fechamento)

        assert conciliacao.esta_conciliado() is False