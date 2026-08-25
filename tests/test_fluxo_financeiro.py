from datetime import date
from financeiro.conta import Conta
from financeiro.categoria import Categoria
from financeiro.lancamento import Lancamento
from financeiro.fechamento import Fechamento
from financeiro.conciliacao import Conciliacao
from financeiro.extrato import Extrato


class TestFluxoFinanceiro:

    def test_fluxo_completo(self) -> None:
        conta = Conta("Conta principal", 1000.0)

        categoria_renda = Categoria("Renda")
        categoria_eletronicos = Categoria("Eletrônicos")

        salario = Lancamento(
            "Salário",
            3000.0,
            date(2026, 8, 5),
            categoria_renda,
            Lancamento.CREDITO,
        )

        teclado = Lancamento(
            "Compra de teclado",
            250.0,
            date(2026, 8, 10),
            categoria_eletronicos,
            Lancamento.DEBITO,
        )

        mouse = Lancamento(
            "Compra de mouse",
            150.0,
            date(2026, 8, 15),
            categoria_eletronicos,
            Lancamento.DEBITO,
        )

        fechamento = Fechamento(
            date(2026, 8, 1),
            date(2026, 8, 31),
            [salario, teclado, mouse],
        )

        conciliacao = Conciliacao(fechamento)

        extrato = Extrato([fechamento])

        assert conta.nome == "Conta principal"
        assert conta.saldo == 1000.0

        assert fechamento.total_creditos() == 3000.0
        assert fechamento.total_debitos() == 400.0
        assert fechamento.saldo() == 2600.0

        assert conciliacao.esta_conciliado() is False

        assert extrato.total() == 3400.0
        assert extrato.total_creditos() == 3000.0
        assert extrato.total_debitos() == 400.0
        assert extrato.saldo() == 2600.0