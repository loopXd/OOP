class Loja:

    taxa = 1.15

    def __init__(self, valor: float) -> None:
        self.valor_do_produto = valor

    def consultar_valor_do_produto(self):
        valor_produto = self.valor_do_produto * self.taxa
        print(f"O valor do produto: {valor_produto}")

    @classmethod
    def editar_taxa_do_produto(cls, valor):
        cls.taxa = valor

loja_praia = Loja(30.50)
loja_shopp = Loja(10.39)
loja_rua = Loja(20.33)

loja_shopp.consultar_valor_do_produto()
loja_rua.consultar_valor_do_produto()
loja_praia.consultar_valor_do_produto()

loja_shopp.editar_taxa_do_produto(1.20)
loja_rua.editar_taxa_do_produto(1.20)
loja_praia.editar_taxa_do_produto(1.20)

loja_shopp.consultar_valor_do_produto()
loja_rua.consultar_valor_do_produto()
loja_praia.consultar_valor_do_produto()
