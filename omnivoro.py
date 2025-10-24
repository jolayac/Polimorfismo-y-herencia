from animales import Animal
class Omnivoro(Animal):
    def __init__(self, nombre, especie):
        super().__init__(nombre, especie, "Omnívoro")

    def alimentarse(self):
        print(f"{self.nombre} come tanto carne como vegetales.")