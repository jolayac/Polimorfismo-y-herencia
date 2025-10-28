from .animal import Animal

class Herbivoro(Animal):
    def __init__(self, nombre, especie):
        super().__init__(nombre, especie, "Herbívoro")

    def alimentarse(self):
        print(f"{self._nombre} se alimenta de plantas, hojas y frutas.")