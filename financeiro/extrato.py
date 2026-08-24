from financeiro.fechamento import Fechamento 

class Extrato: 

    def __init__(self, fechamentos: list[Fechamento]) -> None: 
        self.fechamentos = fechamentos 

    def total(self) -> float: 
        return sum(fechamento.total() for fechamento in self.fechamentos) 