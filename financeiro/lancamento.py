from datetime import date
from financeiro.categoria import Categoria


class Lancamento:

    CREDITO = "CREDITO"
    DEBITO = "DEBITO"

    def __init__(
        self,
        descricao: str,
        valor: float,
        data: date,
        categoria: Categoria,
        tipo: str,
    ) -> None:
        if not descricao.strip():
            raise ValueError("A descrição é obrigatória")

        if valor <= 0:
            raise ValueError("O valor deve ser positivo")

        if tipo not in (self.CREDITO, self.DEBITO):
            raise ValueError("Tipo deve ser CREDITO ou DEBITO")

        self.descricao = descricao
        self.valor = valor
        self.data = data
        self.categoria = categoria
        self.tipo = tipo