from .carnivoro import Carnivoro

class Perro(Carnivoro):
    def __init__(self, nombre):
        super().__init__(nombre, "Perro")

    def moverse(self):
        print(f"{self._nombre} camina sobre cuatro patas.")

    def hablar(self):
        print(f"{self._nombre}: ¡Guau Guau!")