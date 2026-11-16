from abc import ABC, abstractmethod


class EstrategiaFrete(ABC):

    @abstractmethod
    def calcular(self, total: float) -> float:
        pass

