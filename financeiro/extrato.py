from financeiro.fechamento import Fechamento


class Extrato:

    def __init__(self, fechamentos: list[Fechamento]) -> None:
        self.fechamentos = fechamentos

    def total(self) -> float:
        return sum(fechamento.total() for fechamento in self.fechamentos)

    def total_creditos(self) -> float:
        return sum(
            fechamento.total_creditos()
            for fechamento in self.fechamentos
        )

    def total_debitos(self) -> float:
        return sum(
            fechamento.total_debitos()
            for fechamento in self.fechamentos
        )

    def saldo(self) -> float:
        return self.total_creditos() - self.total_debitos()