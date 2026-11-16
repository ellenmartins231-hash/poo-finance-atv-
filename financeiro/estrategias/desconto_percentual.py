from financeiro.estrategias.estrategia_desconto import EstrategiaDesconto


class DescontoPercentual(EstrategiaDesconto):

    def __init__(self, percentual: float) -> None:
        if percentual < 0 or percentual > 100:
            raise ValueError("O desconto deve estar entre 0 e 100")

        self.percentual = percentual

    def calcular(self, total: float) -> float:
        if total < 0:
            raise ValueError("O total não pode ser negativo")

        return total * (self.percentual / 100)
