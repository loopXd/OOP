class Interruptor:

    def __init__(self, comodo: str) -> None:
        self.comodo = comodo

    def acender(self) -> None:
        print(f"Estou acendendo a Luz do {self.comodo}")

    def apagar(self) -> None:
        print(f"Estou apagando a Luz do {self.comodo}")

class Pessoa:

    def acender_luzes(self, interruptor: Interruptor) -> None:
        interruptor.acender()

    def apagar_luzes(self, interruptor: Interruptor) -> None:
        interruptor.apagar()

    def dormir(self) -> None:
        print("A pessoa foi dormir")

murilo = Pessoa()

interruptor_sala = Interruptor("Sala")
interruptor_quarto = Interruptor("Quarto")

murilo.apagar_luzes(interruptor_sala)
murilo.acender_luzes(interruptor_quarto)
