from financeiro.fechamento import Fechamento


class Conciliacao:

    def __init__(self, fechamento: Fechamento) -> None:
        self.fechamento = fechamento

    def esta_conciliado(self) -> bool:
        return self.fechamento.saldo() == 0
        