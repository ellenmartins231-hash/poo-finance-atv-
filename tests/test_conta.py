from financeiro.conta import Conta 

class TestConta: 

    def test_criar_conta_com_nome_e_saldo(self) -> None: 
        conta = Conta("Conta principal", 1300.0)
        assert conta.nome == "Conta principal" 
        assert conta.saldo == 1300.0 