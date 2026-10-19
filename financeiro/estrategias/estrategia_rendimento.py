from abc import ABC, abstractmethod


class EstrategiaRendimento(ABC):

    @abstractmethod
    def calcular(self, valor: float) -> float:
        pass