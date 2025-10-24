from animales import Animal
class Carnivoro(Animal):
    def __init__(self, nombre, especie):
        super().__init__(nombre, especie, "Carnívoro")

    def alimentarse(self):
        print(f"{self.nombre} come carne o alimentos que vengan de otros animales.")