class Conciliacao: 
    def __init__(self, total_debitos: float, total_creditos: float,) -> None: 
        self.total_debitos = total_debitos 
        self.total_creditos = total_creditos

    def esta_conciliado(self) -> bool: 
            return self.total_debitos == self.total_creditos  
        