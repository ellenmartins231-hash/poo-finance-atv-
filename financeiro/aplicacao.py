from financeiro.estrategias.estrategia_rendimento import EstrategiaRendimento


class Aplicacao:

    def __init__(self, valor: float, estrategia: EstrategiaRendimento) -> None:
        if valor < 0:
            raise ValueError("O valor aplicado não pode ser negativo")

        self.valor = valor
        self.estrategia = estrategia

    def calcular_rendimento(self) -> float:
        return self.estrategia.calcular(self.valor)
