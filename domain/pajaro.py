from .herbivoro import Herbivoro

class Pajaro(Herbivoro):
    def __init__(self, nombre):
        super().__init__(nombre, "Pájaro")

    def moverse(self):
        print(f"{self._nombre} vuela con sus alas.")

    def hablar(self):
        print(f"{self._nombre}: Pío pío.")