from financeiro.categoria import Categoria 

class TestCategoria: 
    def test_criar_categoria_com_nome(self) -> None: 
        cat = Categoria("Eletronicos")
        assert cat.nome == "Eletronicos" 