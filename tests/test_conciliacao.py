from financeiro.conciliacao import Conciliacao


class TestConciliacao:

    def test_debitos_e_creditos_iguais_estao_conciliados(self) -> None:
        conciliacao = Conciliacao(1000.0, 1000.0)

        assert conciliacao.esta_conciliado() is True

    def test_debitos_e_creditos_diferentes_nao_estao_conciliados(self) -> None:
        conciliacao = Conciliacao(1000.0, 900.0)

        assert conciliacao.esta_conciliado() is False