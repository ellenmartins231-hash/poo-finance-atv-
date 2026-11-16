from financeiro.estrategias.estrategia_frete import EstrategiaFrete


class FreteFixo(EstrategiaFrete):

    def __init__(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("O valor do frete não pode ser negativo")

        self.valor = valor

    def calcular(self, total: float) -> float:
        if total < 0:
            raise ValueError("O total não pode ser negativo")

        return self.valor
