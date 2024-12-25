class Atendente:

    def __init__(self, atendente: str) -> None:
        self.atendente = atendente

    def atenderChamado(self):
        print(f"O chamado sera atendido por {self.atendente}")

class TI:

    def chamado(self, atendente: Atendente):
        atendente.atenderChamado()
        print(f"O chamado foi finalizado por {atendente.atendente}")

murilo = Atendente("Murilo")
ti = TI()
ti.chamado(murilo)
 