class ConectorBancoDeDados:
    def __init__(self) -> None:
        self.conection = None
    
    def conectarAoBanco(self) -> None:
        self.conection = True

class RepositorioDeBanco:
    def __init__(self, conexao: ConectorBancoDeDados) -> None:
        self.__conexao = conexao

    def buscarDados(self) -> list:
        if self.__conexao.conection:
            return [1, 2, 3, 4, 5]
        return None

class RegraDeNegocio:
    def __init__(self, repo: RepositorioDeBanco):
        self.__repo = repo

    def calcularResultados(self):
        dados = self.__repo.buscarDados()
        if not dados:
            print("dados não encontrados, por favor verifique a conexao com o banco")
        else:
            resposta = 0
            for dado in dados:
                resposta += dado
            print(f"o resultado e: {resposta}")

conn = ConectorBancoDeDados()
conn.conectarAoBanco()

repo = RepositorioDeBanco(conn)
regra = RegraDeNegocio(repo)

regra.calcularResultados()
