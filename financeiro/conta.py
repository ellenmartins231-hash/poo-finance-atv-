class Conta:

    def __init__(self, nome: str, saldo: float) -> None:
        if not nome.strip():
            raise ValueError("O nome da conta é obrigatório")

        if saldo < 0:
            raise ValueError("O saldo não pode ser negativo")

        self.nome = nome
        self.saldo = saldo

    def depositar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo")

        self.saldo += valor

    def sacar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo")

        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")

        self.saldo -= valor