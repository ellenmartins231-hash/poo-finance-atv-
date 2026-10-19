from financeiro.estrategias.estrategia_juros import EstrategiaJuros


class JurosSimples(EstrategiaJuros):

    def __init__(self, taxa: float) -> None:
        if taxa < 0:
            raise ValueError("A taxa de juros não pode ser negativa")

        self.taxa = taxa

    def calcular(self, valor: float, periodos: int) -> float:
        if valor < 0:
            raise ValueError("O valor não pode ser negativo")

        if periodos < 0:
            raise ValueError("O número de períodos não pode ser negativo")

        return valor * (self.taxa / 100) * periodos
