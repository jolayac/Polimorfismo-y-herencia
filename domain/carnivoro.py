from .animal import Animal

class Carnivoro(Animal):
    def __init__(self, nombre, especie):
        super().__init__(nombre, especie, "Carnívoro")

    def alimentarse(self):
        print(f"{self._nombre} come carne o alimentos de animales.")