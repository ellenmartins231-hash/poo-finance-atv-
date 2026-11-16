from financeiro.estrategias.estrategia_desconto import EstrategiaDesconto


class SemDesconto(EstrategiaDesconto):

    def calcular(self, total: float) -> float:
        if total < 0:
            raise ValueError("O total não pode ser negativo")

        return 0
