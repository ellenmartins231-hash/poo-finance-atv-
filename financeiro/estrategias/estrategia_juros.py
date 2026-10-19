from abc import ABC, abstractmethod


class EstrategiaJuros(ABC):

    @abstractmethod
    def calcular(self, valor: float, periodos: int) -> float:
        pass
