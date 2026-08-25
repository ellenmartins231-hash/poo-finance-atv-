from datetime import date
from financeiro.lancamento import Lancamento


class Fechamento:

    def __init__(
        self,
        data_inicio: date,
        data_fim: date,
        lancamentos: list[Lancamento],
    ) -> None:
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.lancamentos = lancamentos

    def total(self) -> float:
        return sum(lancamento.valor for lancamento in self.lancamentos)

    def total_creditos(self) -> float:
        return sum(
            lancamento.valor
            for lancamento in self.lancamentos
            if lancamento.tipo == Lancamento.CREDITO
        )

    def total_debitos(self) -> float:
        return sum(
            lancamento.valor
            for lancamento in self.lancamentos
            if lancamento.tipo == Lancamento.DEBITO
        )

    def saldo(self) -> float:
        return self.total_creditos() - self.total_debitos()