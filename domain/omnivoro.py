from .animal import Animal

class Omnivoro(Animal):
    def __init__(self, nombre, especie):
        super().__init__(nombre, especie, "Omnívoro")

    def alimentarse(self):
        print(f"{self._nombre} come tanto carne como vegetales.")