from abc import ABC, abstractmethod


class EstrategiaDesconto(ABC):

    @abstractmethod
    def calcular(self, total: float) -> float:
        pass
