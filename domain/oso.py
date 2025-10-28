from .omnivoro import Omnivoro

class Oso(Omnivoro):
    def __init__(self, nombre):
        super().__init__(nombre, "Oso")

    def moverse(self):
        print(f"{self._nombre} camina en cuatro patas, a veces en dos.")

    def hablar(self):
        print(f"{self._nombre}: GRRRRR.")