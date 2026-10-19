from financeiro.estrategias.estrategia_rendimento import EstrategiaRendimento


class RendimentoCDB(EstrategiaRendimento):

    def __init__(self, taxa: float) -> None:
        if taxa < 0:
            raise ValueError("A taxa de rendimento não pode ser negativa")

        self.taxa = taxa

    def calcular(self, valor: float) -> float:
        if valor < 0:
            raise ValueError("O valor aplicado não pode ser negativo")

        return valor * (self.taxa / 100)