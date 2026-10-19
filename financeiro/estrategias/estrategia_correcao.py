from abc import ABC, abstractmethod


class EstrategiaCorrecao(ABC):

    @abstractmethod
    def calcular(self, valor: float) -> float:
        pass
