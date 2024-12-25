class ConectorBancoDeDados:
    def __init__(self) -> None:
        self.conection = None
    
    def conectarAoBanco(self) -> None:
        self.conection = True

class RepositorioDeBanco:
    def __init__(self, conexao: ConectorBancoDeDados, user: str) -> None:
        self.__user = user
        self.__conexao = conexao

    def buscarDados(self) -> str:
        if self.__conexao.conection:
            return self.__user
        return None

class RegraDeNegocio:
    def __init__(self, repo: RepositorioDeBanco):
        self.__repo = repo

    def calcularResultados(self):
        dados = self.__repo.buscarDados()
        if not dados:
            print("dados não encontrados, por favor verifique a conexao com o banco")
        else:
            print(f"o resultado e: {dados}")

conn = ConectorBancoDeDados()
#conn.conectarAoBanco()

dado = str(input("Digite seu nome: "))
repo = RepositorioDeBanco(conn, dado)
regra = RegraDeNegocio(repo)

regra.calcularResultados()