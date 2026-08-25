from datetime import date
from financeiro.categoria import Categoria
from financeiro.lancamento import Lancamento


class TestLancamento:

    def test_criar_lancamento_com_atributos(self) -> None:
        categoria = Categoria("Eletronicos")
        data = date(2026, 8, 19)

        lancamento = Lancamento(
            "Compra de teclado",
            240.0,
            data,
            categoria,
            Lancamento.DEBITO
        )

        assert lancamento.descricao == "Compra de teclado"
        assert lancamento.valor == 240.0
        assert lancamento.data == data
        assert lancamento.categoria is categoria
        assert lancamento.tipo == Lancamento.DEBITO

    def test_criar_lancamento_com_credito(self) -> None:
        categoria = Categoria("Salario")
        data = date(2026, 8, 19)

        lancamento = Lancamento(
            "Salario",
            3000.0,
            data,
            categoria,
            Lancamento.CREDITO
        )

        assert lancamento.tipo == Lancamento.CREDITO

    def test_lancamento_com_valor_zero(self) -> None:
        categoria = Categoria("Eletronicos")
        data = date(2026, 8, 19)

        try:
            Lancamento(
                "Compra",
                0,
                data,
                categoria,
                Lancamento.DEBITO
            )
            assert False, "Deveria ter lançado exceção"
        except ValueError:
            pass

    def test_lancamento_com_valor_negativo(self) -> None:
        categoria = Categoria("Eletronicos")
        data = date(2026, 8, 19)

        try:
            Lancamento(
                "Compra",
                -100.0,
                data,
                categoria,
                Lancamento.DEBITO
            )
            assert False, "Deveria ter lançado exceção"
        except ValueError:
            pass

    def test_lancamento_com_tipo_invalido(self) -> None:
        categoria = Categoria("Eletronicos")
        data = date(2026, 8, 19)

        try:
            Lancamento(
                "Compra",
                240.0,
                data,
                categoria,
                "INVALIDO"
            )
            assert False, "Deveria ter lançado exceção"
        except ValueError:
            pass

    def test_lancamento_com_descricao_vazia(self) -> None:
        categoria = Categoria("Eletronicos")
        data = date(2026, 8, 19)

        try:
            Lancamento(
                "",
                240.0,
                data,
                categoria,
                Lancamento.DEBITO
            )
            assert False, "Deveria ter lançado exceção"
        except ValueError:
            pass

    def test_lancamento_com_descricao_apenas_espacos(self) -> None:
        categoria = Categoria("Eletronicos")
        data = date(2026, 8, 19)

        try:
            Lancamento(
                "   ",
                240.0,
                data,
                categoria,
                Lancamento.DEBITO
            )
            assert False, "Deveria ter lançado exceção"
        except ValueError:
            pass