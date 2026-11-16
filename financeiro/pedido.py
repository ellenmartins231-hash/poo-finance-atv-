from datetime import date

from financeiro.cupom import Cupom
from financeiro.estrategias.estrategia_frete import EstrategiaFrete


class Pedido:

    def __init__(
        self,
        total: float,
        estrategia_frete: EstrategiaFrete,
        cupom: Cupom = None
    ) -> None:
        if total < 0:
            raise ValueError("O total do pedido não pode ser negativo")

        self.total = total
        self.estrategia_frete = estrategia_frete
        self.cupom = cupom

    def calcular_valor_final(self, hoje: date = None) -> float:
        desconto = 0

        if self.cupom is not None:
            desconto = self.cupom.calcular_desconto(self.total, hoje)

        total_com_desconto = self.total - desconto
        frete = self.estrategia_frete.calcular(total_com_desconto)

        return total_com_desconto + frete
