from datetime import date

from financeiro.lancamento import Lancamento 

class Fechamento: 

    def __init__(self, data_inicio: date, data_fim: date, lancamentos: list[Lancamento]) -> None: 

        self.data_inicio = data_inicio 
        self.data_fim = data_fim 
        self.lancamentos = lancamentos 

    def total(self) -> float: 
            return sum(lancamento.valor for lancamento in self.lancamentos)