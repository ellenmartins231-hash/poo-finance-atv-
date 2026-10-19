from financeiro.estrategias.estrategia_correcao import EstrategiaCorrecao


class CorrecaoIPCA(EstrategiaCorrecao):

    def __init__(self, taxa: float) -> None:
        if taxa < 0:
            raise ValueError("A taxa de correção não pode ser negativa")

        self.taxa = taxa

    def calcular(self, valor: float) -> float:
        if valor < 0:
            raise ValueError("O valor não pode ser negativo")

        return valor * (1 + self.taxa / 100)
