import pytest

from financeiro.conta import Conta


class TestConta:

    def test_criar_conta_com_nome_e_saldo(self) -> None:
        conta = Conta("Conta principal", 1300.0)

        assert conta.nome == "Conta principal"
        assert conta.saldo == 1300.0

    def test_criar_conta_com_saldo_zero(self) -> None:
        conta = Conta("Conta principal", 0.0)

        assert conta.saldo == 0.0

    def test_nao_permitir_saldo_inicial_negativo(self) -> None:
        with pytest.raises(ValueError):
            Conta("Conta principal", -100.0)

    def test_nao_permitir_nome_vazio(self) -> None:
        with pytest.raises(ValueError):
            Conta("", 100.0)

    def test_depositar_valor(self) -> None:
        conta = Conta("Conta principal", 1000.0)

        conta.depositar(500.0)

        assert conta.saldo == 1500.0

    def test_nao_permitir_deposito_zero(self) -> None:
        conta = Conta("Conta principal", 1000.0)

        with pytest.raises(ValueError):
            conta.depositar(0.0)

    def test_nao_permitir_deposito_negativo(self) -> None:
        conta = Conta("Conta principal", 1000.0)

        with pytest.raises(ValueError):
            conta.depositar(-100.0)

    def test_sacar_valor(self) -> None:
        conta = Conta("Conta principal", 1000.0)

        conta.sacar(300.0)

        assert conta.saldo == 700.0

    def test_nao_permitir_saque_zero(self) -> None:
        conta = Conta("Conta principal", 1000.0)

        with pytest.raises(ValueError):
            conta.sacar(0.0)

    def test_nao_permitir_saque_negativo(self) -> None:
        conta = Conta("Conta principal", 1000.0)

        with pytest.raises(ValueError):
            conta.sacar(-100.0)

    def test_nao_permitir_saque_maior_que_saldo(self) -> None:
        conta = Conta("Conta principal", 1000.0)

        with pytest.raises(ValueError):
            conta.sacar(1500.0)

        assert conta.saldo == 1000.0