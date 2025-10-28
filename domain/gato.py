from .carnivoro import Carnivoro

class Gato(Carnivoro):
    def __init__(self, nombre):
        super().__init__(nombre, "Gato")

    def moverse(self):
        print(f"{self._nombre} camina sobre cuatro patas.")

    def hablar(self):
        print(f"{self._nombre}: Miauuu.")