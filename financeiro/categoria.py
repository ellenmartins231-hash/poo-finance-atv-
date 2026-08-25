class Categoria:

    def __init__(self, nome: str) -> None:
        if not nome.strip():
            raise ValueError("O nome da categoria é obrigatório")

        self.nome = nome