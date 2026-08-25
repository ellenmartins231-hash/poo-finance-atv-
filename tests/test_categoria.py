import pytest

from financeiro.categoria import Categoria


class TestCategoria:

    def test_criar_categoria_com_nome(self) -> None:
        cat = Categoria("Eletronicos")

        assert cat.nome == "Eletronicos"

    def test_nao_permitir_categoria_sem_nome(self) -> None:
        with pytest.raises(ValueError):
            Categoria("")

    def test_nao_permitir_categoria_com_apenas_espacos(self) -> None:
        with pytest.raises(ValueError):
            Categoria("")