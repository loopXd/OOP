class Produto:
    def __init__(self, nome: str, valor: int|float) -> None:
        self.__nome = nome
        self.__valor = valor

    def infoProduto(self) -> None:
        print(f" Produto: {self.__nome}  Valor: {self.__valor} ")

class CarrinhoDeCompras:
    def __init__(self) -> None:
        self.__produtos = []
    
    def addProduto(self, produto: Produto):
        self.__produtos.append(produto)
    
    def finalizarCompra(self) -> None:
        print("Compra finalizada")
        print("     Produtos:   ")
        for product in self.__produtos:
            product.infoProduto()

banana = Produto("banana", 33)
uva = Produto("uva", 24)
pera = Produto("pera", 15)

carrinho = CarrinhoDeCompras()
carrinho.addProduto(banana)
carrinho.addProduto(pera)
carrinho.addProduto(uva)

carrinho.finalizarCompra()
