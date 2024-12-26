class ConnectionDB:
    def conectar(self):
        print("Conectando ao banco")

class SqlRepository(ConnectionDB):
    def select(self):
        print("Buscando dados no banco SQL")

class NoSqlRepository(ConnectionDB):
    def select(self):
        print("Buscando dados no banco NoSQL")

class DBHandler():
    def altertable(self):
        print("Alterando tabela em SQL")
