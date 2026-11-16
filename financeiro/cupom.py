from datetime import date

from financeiro.estrategias.estrategia_desconto import EstrategiaDesconto


class Cupom:

    def __init__(self, estrategia: EstrategiaDesconto, validade: date) -> None:
        self.estrategia = estrategia
        self.validade = validade

    def calcular_desconto(self, total: float, hoje: date = None) -> float:
        if hoje is None:
            hoje = date.today()

        if hoje > self.validade:
            raise ValueError("O cupom está vencido")

        return self.estrategia.calcular(total)
