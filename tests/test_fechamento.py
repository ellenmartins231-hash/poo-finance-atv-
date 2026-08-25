from datetime import date
from financeiro.categoria import Categoria
from financeiro.lancamento import Lancamento
from financeiro.fechamento import Fechamento


class TestFechamento:

    def setup_method(self) -> None:
        self.categoria = Categoria("Eletrônicos")
        self.data = date(2026, 8, 19)

    def test_calcular_total_dos_lancamentos(self) -> None:
        lancamento1 = Lancamento(
            "Compra de teclado",
            250.0,
            self.data,
            self.categoria,
            Lancamento.DEBITO,
        )

        lancamento2 = Lancamento(
            "Compra de mouse",
            150.0,
            self.data,
            self.categoria,
            Lancamento.DEBITO,
        )

        fechamento = Fechamento(
            self.data,
            self.data,
            [lancamento1, lancamento2],
        )

        assert fechamento.total() == 400.0

    def test_calcular_total_dos_creditos(self) -> None:
        salario = Lancamento(
            "Salário",
            3000.0,
            self.data,
            self.categoria,
            Lancamento.CREDITO,
        )

        freelance = Lancamento(
            "Freelance",
            500.0,
            self.data,
            self.categoria,
            Lancamento.CREDITO,
        )

        fechamento = Fechamento(
            self.data,
            self.data,
            [salario, freelance],
        )

        assert fechamento.total_creditos() == 3500.0

    def test_calcular_total_dos_debitos(self) -> None:
        teclado = Lancamento(
            "Compra de teclado",
            250.0,
            self.data,
            self.categoria,
            Lancamento.DEBITO,
        )

        mouse = Lancamento(
            "Compra de mouse",
            150.0,
            self.data,
            self.categoria,
            Lancamento.DEBITO,
        )

        fechamento = Fechamento(
            self.data,
            self.data,
            [teclado, mouse],
        )

        assert fechamento.total_debitos() == 400.0

    def test_calcular_saldo(self) -> None:
        salario = Lancamento(
            "Salário",
            3000.0,
            self.data,
            self.categoria,
            Lancamento.CREDITO,
        )

        teclado = Lancamento(
            "Compra de teclado",
            250.0,
            self.data,
            self.categoria,
            Lancamento.DEBITO,
        )

        mouse = Lancamento(
            "Compra de mouse",
            150.0,
            self.data,
            self.categoria,
            Lancamento.DEBITO,
        )

        fechamento = Fechamento(
            self.data,
            self.data,
            [salario, teclado, mouse],
        )

        assert fechamento.saldo() == 2600.0

    def test_fechamento_sem_lancamentos(self) -> None:
        fechamento = Fechamento(
            self.data,
            self.data,
            [],
        )

        assert fechamento.total() == 0.0
        assert fechamento.total_creditos() == 0.0
        assert fechamento.total_debitos() == 0.0
        assert fechamento.saldo() == 0.0