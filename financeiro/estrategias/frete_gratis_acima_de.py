from financeiro.estrategias.estrategia_frete import EstrategiaFrete


class FreteGratisAcimaDe(EstrategiaFrete):

    def __init__(self, valor_minimo: float, valor_frete: float) -> None:
        if valor_minimo < 0:
            raise ValueError("O valor mínimo não pode ser negativo")

        if valor_frete < 0:
            raise ValueError("O valor do frete não pode ser negativo")

        self.valor_minimo = valor_minimo
        self.valor_frete = valor_frete

    def calcular(self, total: float) -> float:
        if total < 0:
            raise ValueError("O total não pode ser negativo")

        if total >= self.valor_minimo:
            return 0

        return self.valor_frete
